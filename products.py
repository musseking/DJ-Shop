import admin, __main__, autenti
from autenti import *
import json

with open("products.json", "r") as prod:
    products = json.load(prod)



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
    menu()

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
    names = list(__main__.userCart.keys())
    for i, x in enumerate(names):
        print(f"{i}) {x}")
    
    delete = int(input("Line to delete: "))
    del __main__.userCart[names[delete]]
    
    print("Successfully deleted!")
    userMenu()

def showCart():

    if not __main__.userCart:
        print("Your cart is empty!")
        return
    
    for name, value in __main__.userCart.items():
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

def buy():
    pass

def addToCart():
    user = __main__.currentUser

    names = list(products.keys())
    for i, x in enumerate(names):
        print(f"{i}) {x}")
    
    index = int(input("Index of product to add: "))

    qt = int(input("Quantity to add: "))
    
    '''if not(__main__.userCart):
        __main__.userCart = {}'''
    
    item = names[index]
    if not __main__.userCart.get(item):
        __main__.userCart[item] = 0

    __main__.userCart[item] += qt

    autenti.saveCart(__main__.currentUser)
    
    print("Successfully added")

    print()
    userMenu()