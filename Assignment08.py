# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# mkoj,06.08.2020,Added main body of script
# mkoj,06.08.2020,Added FileProcessor methods
# mkoj,06.08.2020,Added IO methods
# mkoj,06.09.2020,Added Product class pattern
# mkoj,06.09.2020,Added comments and docstrings
# ------------------------------------------------------------------------ #

import pickle

# Data -------------------------------------------------------------------- #

strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ""
objFile = None  # An object that represents a file

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
        add():
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        mkoj,06.08.2020,Added the add() method
    """

    # -- Fields --
    # -- Constructor --
    def __init__(self, product_name, product_price):
        #     -- Attributes --
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        self.__product_name = value

    @property
    def product_price(self):
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        self.__product_price = value

    # -- Methods --
    def __str__(self):
        return self.product_name + " ($" + str(self.product_price) + ")"


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(self, file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        mkoj,06.08.2020,Added save_data_to_file and read_data_from_file methods
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Saves data from list_of_product_objects into a pickled text file
        :param list_of_product_objects: List of objects
        :param file_name: (string) with name of file
        """
        pickle_out = open(file_name, "wb")
        pickle.dump(list_of_product_objects, pickle_out)
        pickle_out.close()

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """ Reads data from a file into list of rows
        :param list_of_product_objects: List of objects
        :param file_name: (string) with name of file
        """
        list_of_product_objects.clear()
        try:
            pickle_in = open(file_name, "rb+")
            data_from_file = pickle.load(pickle_in)
            pickle_in.close()
            return data_from_file
        except:
            print("No existing data in file \"products.txt\"")
            return []  # Prevents list from being accidentally designated NoneType


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Processes data to and from a file and a list of product objects:
    methods:
        print_menu(): Prints a menu of options to the user
        menu_choice():
        show_data():
        new_product():
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        mkoj,06.08.2020,Added print_menu() menu_choice() and show_data() methods
    """

    @staticmethod
    def print_menu():
        """Prints menu of options for the user
        """
        print('''
                Options:
                1) See current data
                2) Add a product
                3) Save and exit
                ''')

    @staticmethod
    def menu_choice():
        """Prompts user to make a menu choice
        return: string of user selection
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def show_data(list_of_product_objects):
        """Prints objects in list_of_product_objects back to user, cleaned up
        return: string of user selection
        """
        print("******* Current data *******")
        for row in list_of_product_objects:
            print(row)
        print("****************************")

    @staticmethod
    def new_product(list_of_product_objects):
        p_name = input("Product Name: ").strip()
        p_price = input("Product Price: ").strip()
        while True:
            try:
                p_price = float(p_price)
                break
            except:
                print("Price must be a number.")
                p_price = input("Product Price: ").strip()
        list_new_product = Product(product_name=p_name, product_price=p_price)
        list_of_product_objects.append(list_new_product)


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)  # read file data into lstOfProductObjects list

while (True):
    # Show user a menu of options
    IO.print_menu()
    # Get user's menu option choice
    strChoice = IO.menu_choice()
    if strChoice.strip() == '1':  # Show user current data in the list of product objects
        IO.show_data(lstOfProductObjects)
    elif strChoice.strip() == '2':  # Let user add data to the list of product objects
        IO.new_product(lstOfProductObjects)
    elif strChoice.strip() == '3':  # let user save current data to file and exit program
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print("Data saved to file.")
        break
    else:  # Catches invalid menu responses
        print("Invalid selection, press [ENTER] to continue.")

input('\n\nPress the [Enter] key to continue.')
# Main Body of Script  ---------------------------------------------------- #
