import auth, __main__, json

import products


def addProduct():
    productName = input("Product name: ")
    productBrand = input("Product brand: ")
    productPrice = float(input("Product price: "))
    productQuantity = int(input("Product quantity: "))

    products.products[productName] = {
        "brand": productBrand,
        "price": productPrice,
        "quantity": productQuantity
    }
    with open("products.json", "w", encoding="utf8") as prod:
        json.dump(products.products, prod)
        
    print()
    adminMenu()

def deleteProduct():
    names = list(products.products.keys())
    for i, x in enumerate(names):
        print(f"{i}) {x}")
    
    delete = int(input("Line to delete: "))
    del products.products[names[delete]]
    
    print("Successfully deleted!")
    adminMenu()


def listProducts():

    functions = {
        "1": showAll,
        "2": search,
        "X": exit
    }
    option = None
    while not option in functions.keys():
        print("(1) Show all products")
        print("(2) Search")
        option = input().upper()

    return functions[option]()

def back1():
    adminMenu()

def back2():
   __main__.main()

def adminMenu1():
    functions = {
        "1": addProduct,
        "2": deleteProduct,
        "3": back1
    }

    action = None
    while not action in functions.keys():
        print("(1) Add a product")
        print("(2) Delete product")
        print("(3) Back")
        action  = input().upper()

    functions[action]()

def adminMenu():
    functions = {
        "1": addProduct,
        "2": deleteProduct,
        "3": listProducts,
        "4": orderList,
        "5": back2,
        "X": exit
    }

    action = None
    while not action in functions.keys():
        print("(1) Add a product")
        print("(2) Remove product")
        print("(3) List of products")
        print("(4) Order list")
        print("(5) Log out")
        print("(X) Exit")
        action  = input().upper()

    functions[action]()

def orderList():
    pass

def showAll():
    for name, values in products.products.items():
        print(name, values["brand"], values["price"], values["quantity"], sep="\t")

    adminMenu1()

def search():
    term = input("Search: ").lower()
    for name, values in products.products.items():
        if term in name.lower():
            print(name, values["brand"], values["price"], values["quantity"], sep="\t")

    adminMenu()