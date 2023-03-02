import main
import auth, admin

def search():
    term = input("Search: ")
    with open("products.txt", "r") as f:
        for line in f.readlines():
            if term in line:
                print("\n" + line)

    userMenu()

def showAll():
    with open("products.txt", "r") as f:
        for i, line in enumerate(f):
            print("{0}) {1}".format(i+1, line))

    userMenu()

def allProducts():

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

def cart():
    pass

def back():
    main.main()

def userMenu():

    functions = {
        "1": allProducts,
        "2": cart,
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