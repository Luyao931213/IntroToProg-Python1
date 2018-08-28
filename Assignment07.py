# -------------------------------------------------#
# Title: Working with errors and pickling
# Dev:   Luyao Xu
# Date:  08/28/2018
# Desc: Furniture sale list
# ChangeLog:Luyao, 08/28/2018,  Create a simple example  of Python Exception handling and pickling.
# -------------------------------------------------#
'''
1)	Create a simple example of how you would use Python Exception Handling. Make sure to comment your code.

2)	Create a simple example of how you would use Python Pickling. Make sure to comment your code.

'''

# --Data--#

# declare variables and constants
# f = An object that represents a file
# name_input= Input of the name of furniture
# price_input= Input of a price the furniture

# --Processing--#

import pickle

FURNITURE = []  # create a global list to save furniture

# define the method
def add_furniture():
    print("Please input a furniture you want to sale, and list its price.")  # capture user input
    print("Enter 'Exit' to quite.")  # Program exit when user input 'exit'.
    while True:
        name_input = input("Please enter a furniture you want to sell: ")
        if name_input.lower() == 'exit': # if user input'exit', program exit
            break
        else:
            price_input = float(input("Please enter the price of the furniture: "))  # possible point of exception
            FURNITURE.append([name_input, price_input])  # append to global list


# Save data to the file using pickle
def dump_data(furniture, filename):
    f = open(filename, 'wb')  # Create and write into a binary file
    pickle.dump(furniture, f)  # dump the text contents to f
    f.close()  # File close


# Read data with pickle from a binary file
def load_data(filename):
    f = open(filename, 'rb')  # open and read text from the binary file
    data = pickle.load(f)  # Load data from f
    f.close()  # File close
    return data


# Error handling
#--Presentation--#
try:
    add_furniture()
    dump_data(FURNITURE, 'furniture.dat')
    file_content = load_data('furniture.dat')

    # format and print the items in the file
    print('Here is a summary of what you want to sell:')
    for i in file_content:
        print(i[0] + ' for $' + str(i[1]))


except Exception as e:  # capture exception and print the error
    print('An error has occurred:')
    print(e)
