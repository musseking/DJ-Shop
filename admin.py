import auth, main

def addProduct():
    productName = input("Product name: ")
    productBrand = input("Product brand: ")
    productPrice = float(input("Product price: "))
    productQuantity = int(input("Product quantity: "))

    with open("products.txt", "a") as prod:
        prod.write(productName + "|" + productBrand + "|" + str(productPrice) + "|" + str(productQuantity) + "\n")
    print()
    adminMenu()

def deleteProduct():
    a = None

    with open("products.txt", "r") as f:
        for i, line in enumerate(f):
            print("{0}) {1}".format(i+1, line))

        f.seek(0)
        a = f.readlines()
        print(a)
            
        delete = int(input("Line to delete: "))
        a.pop(delete - 1)

    with open("products.txt", "w") as f:
        f.write(''.join(a))
    
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
   main.main()

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
        "4": back2,
        "X": exit
    }

    action = None
    while not action in functions.keys():
        print("(1) Add a product")
        print("(2) Remove product")
        print("(3) List of products")
        print("(4) Log out")
        print("(X) Exit")
        action  = input().upper()

    functions[action]()

def showAll():
    with open("products.txt", "r") as f:
        for i, line in enumerate(f):
            print("{0}) {1}".format(i+1, line))

    adminMenu1()

def search():
    term = input("Search: ")
    with open("products.txt", "r") as f:
        for line in f.readlines():
            if term in line:
                print("\n" + line)

    adminMenu()