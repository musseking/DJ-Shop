import __main__, auth, admin
import json

with open("products.json", "r") as prod:
    products = json.load(prod)

with open("usercart.json", "r") as cart:
    korpa = json.load(cart)

def search():
    term = input("Search: ").lower()
    for name, values in products.products.items():
        if term in name.lower():
            print(name, values["brand"], values["price"], values["quantity"], sep="\t")

    userMenu()

def showAll():
    for name, values in products.items():
        print(name, values["brand"], values["price"], values["quantity"], sep="\t" + "\n")

    userMenuBuy()

def allProducts():

    functions = {
        "1": showAll,
        "2": search,
        "3": userMenu,
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
    __main__.main()

def userMenuBuy():
    
    functions = {
        "1": addToCart,
        "2": showCart,
        "3": userMenu
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
        print("(3) Log out")
        print("(X) Exit")
        action  = input().upper()

    return functions[action]()

def RemoveItem():
    names = list(korpa[__main__.currentUser].keys())
    for i, x in enumerate(names):
        print(f"{i}) {x}")
    
    delete = int(input("Line to delete: "))
    del korpa[__main__.currentUser][names[delete]]
    
    print("Successfully deleted!")
    userMenu()

def showCart():

    if not korpa.get(__main__.currentUser):
        print("Your cart is empty!")
        return
    
    for name, value in korpa[__main__.currentUser].items():
        print(name, value, sep="\t")

    function = {
        "1": RemoveItem,
        "X": userMenu}

    action = None
    while not action in function.keys():
        print("\n(1) Remove Item")
        print("(x) Back")
        action = input().upper()

    return function[action]()


def addToCart():
    user = __main__.currentUser

    names = list(products.keys())
    for i, x in enumerate(names):
        print(f"{i}) {x}")
    
    index = int(input("Index of product to add: "))

    qt = int(input("Import quantity: "))
    
    if not(korpa.get(user)):
        korpa[user] = {}
    
    item = names[index]
    if not korpa[user].get(item):
        korpa[user][item] = 0

    korpa[user][item] += qt

    with open("usercart.json", "w", encoding="utf8") as f:
        json.dump(korpa, f)
    
    print("Successfully added")

    print()
    userMenu()