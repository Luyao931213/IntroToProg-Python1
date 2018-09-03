# --Class Definitions--#
class Product(object):
    """Class for product data"""

    # --Fields--#
    # pid: Product ID
    # name: Product name
    # price: Product Price
    # --Constructor--#
    def __init__(self, pid, name, price):
        # --Attributes--#
        self.pid = pid
        self.name = name
        self.price = price

    # --string representation method--#
    def __str__(self):
        return ','.join([self.pid, self.name, self.price])


class ProductIO(object):

    def __init__(self, file_object, products):
        self.products = products
        self.file_object = file_object

    # write products to file object on exit
    def write(self):
        try:
            print("Type in a Product Id, Name, and Price you want to add to the file")
            print("(Enter 'Exit' to quit!)")
            while True:
                user_input = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
                if user_input.lower() == "exit":
                    break
                else:
                    pid, name, price = user_input.split(',')
                    self.products.append(Product(id, name, price))

            for product in self.products:
                self.file_object.write(str(product) + "\n")
        except Exception as ex:
            print("Error: " + str(ex))

    # read file content
    def read(self, message="Contents of File"):
        try:
            print(message)
            self.file_object.seek(0)
            print(self.file_object.read())
        except Exception as ex:
            print("Error: " + str(ex))


if __name__ == '__main__':
    # Data
    file_obj = None  # File Handle

    # I/O
    try:
        file_obj = open("Products.txt", "r+")
        io = ProductIO(file_obj, [])
        io.read("Here is the current data:")
        io.write()
        io.read("Here is this data was saved:")
    except FileNotFoundError as e:
        print("Error: " + str(e) + "\n Please check the file name")
    except Exception as e:
        print("Error: " + str(e))
    finally:
        if file_obj is not None:
            file_obj.close()
