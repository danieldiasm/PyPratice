## This is a playground to test things related to classes and methods.

class Store:
    def __init__(self, name, founder):
        self.name = name
        self.founder = founder
        self.productList = []
    
    def addProduct(self, product, price):
        self.productList.append({'product':product,'price':price})

def listProduct():
    pass
def addProduct():
    pass
def addStore():
    pass
def removeProduct():
    pass
def listStore():
    pass

menuOptions = {1:"listProduct", 2:"addProduct", 3:"removeProduct" ,4:"addStore", 5:"listStore"}
menuSeparator = "+---------------------------------+"

while True:
    print(menuSeparator)
    print("| Choose an option:")
    print("| 1 - List Products")
    print("| 2 - Add a Product")
    print("| 3 - Remove a Product")
    print("| 4 - Add a Store")
    print("| 5 - List and Select Store")
    print("| 0 - Exit")
    print(menuSeparator)
    opt = input("Option: ")

    if int(opt) in menuOptions:
        if opt == 1:
            listProduct()
        elif opt == 2:
            addProduct()
        elif opt == 3:
            removeProduct()
        elif opt == 4:
            addStore()
        elif opt == 5:
            listStore()
        else:
            pass
    elif int(opt) == 0:
        break
    else:
        print("Not Available")


    