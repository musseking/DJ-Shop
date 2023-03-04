import main
import auth, admin

def search():
    term = input("Search: ")
    with open("products.txt", "r") as f:
        for line in f.readlines():
            if term in line:
                print("\n" + line)
            else: 
                print("\nThere is no such product.")
                break

    userMenu()

def showAll():
    with open("products.txt", "r") as f:
        for i, line in enumerate(f):
            print("{0}) {1}".format(i+1, line))

    userMenuBuy()

def BackToUserMenu():
    userMenu()

def allProducts():

    functions = {
        "1": showAll,
        "2": search,
        "3": BackToUserMenu,
        "X": exit
    }
    option = None
    while not option in functions.keys():
        print("(1) Show all products")
        print("(2) Search")
        print("(3) Back")
        option = input().upper()

    return functions[option]()

def back():
    main.main()

def userMenuBuy():
    
    functions = {
        "1": addToCart,
        "2": showCart,
        "3": BackToUserMenu
    }

    action = None
    while not action in functions.keys():
        print("(1) Add To Cart")
        print("(2) My cart")
        print("(3) Back")
        action  = input().upper()

    return functions[action]()


def userMenu():

    functions = {
        "1": allProducts,
        "2": showCart,
        "3": back,
        "X": exit
    }

    action = None
    while not action in functions.keys():
        print("(1) See All Products")
        print("(2) My cart")
        print("(3) Back")
        print("(X) Exit")
        action  = input().upper()

    return functions[action]()

def RemoveItem():
    a = None

    with open("usercart.txt", "r") as f:
        for i, line in enumerate(f):
            print("{0}) {1}".format(i+1, line))

        f.seek(0)
        a = f.readlines()
        #print(a)
            
        delete = int(input("Line to delete: "))
        a.pop(delete - 1)

    with open("usercart.txt", "w") as f:
        f.write(''.join(a))
    
    print("Successfully deleted!")
    userMenu()

def showCart():
    with open("usercart.txt", "r") as f:
        f.seek(0)
        line = f.read(1)
        if not line:
            print("\nYour cart is empty!")
        else:
            f.seek(0)
            for i, line in enumerate(f):
                print("{0}) {1}".format(i+1, line))

    function = {
        "1": RemoveItem,
        "X": userMenu}

    action = None
    while not action in function.keys():
        print("(1) Remove Item")
        print("(x) Back")
        action = input().upper()

    return function[action]()


def addToCart():
    productName = input("Enter product name: ")
    productQuantity = input("Enter quantity: ")
    with open("usercart.txt", "a") as f:
        f.write(productName + "|" + productQuantity )

    print()
    userMenu()