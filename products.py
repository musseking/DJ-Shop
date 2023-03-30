import admin, __main__, autenti, graphs
from autenti import *
import json

with open("products.json", "r") as prod:
    products = json.load(prod)


def search():
    term = input("Search: ").lower()
    for name, values in products.items():
        if term in name.lower():
            print(f'Name: {name:30}', f'Brand: {values["brand"]:30}', f'Price: {values["price"]:13.2f} RSD', f'Quantity: {values["quantity"]:7}', sep="\t")
    
    print()
    userMenuBuy()

def showAll():
    for name, values in products.items():
        print(f'Name: {name:30}', f'Brand: {values["brand"]:30}', f'Price: {values["price"]:13.2f} RSD', f'Quantity: {values["quantity"]:7}', sep="\t")
    print()
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

def logout():
    __main__.currentUser = None
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

def userSales():
    graphs.userSales(__main__.currentUser)
    userMenu()

def userMenu():

    functions = {
        "1": allProducts,
        "2": showCart,
        "3": userSales,
        "4": logout,
        "X": exit
    }

    action = None
    while not action in functions.keys():
        print("(1) See All Products")
        print("(2) My cart")
        print("(3) Graphs of your purchases")
        print("(4) Log out")
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
    return

def EditQty():
    names = list(__main__.userCart.keys())
    for i, x in enumerate(names):
        print(f"{i}) {x}")
    
    line = int(input("Line to edit: "))
    qty = int(input("Enter new quantity: "))
    if qty > products[names[line]]["quantity"] or qty < 0:
        print("Invalid quantity!\n")
        userMenu()
        return

    __main__.userCart[names[line]] = qty
    
    print("Successfully edited!\n")
    userMenu()
    return

def showCart():
    if not __main__.userCart:
        print("Your cart is empty!\n")
        userMenu()
        return
    
    totalPrice = 0
    for name, value in __main__.userCart.items():
        itemTotal = products[name]["price"] * value
        totalPrice += itemTotal
        print(f'Name: {name:30}', f'Brand: {products[name]["brand"]:30}', f'Price: {products[name]["price"]:13.2f} RSD', f'Quantity: {value:7}', f'Total: {itemTotal:13.2f} RSD', sep="\t")

    print(f'Total cart price: {totalPrice:.2f} RSD')

    function = {
        "1": buy,
        "2": RemoveItem,
        "3": EditQty,
        "X": userMenu
    }

    action = None
    while not action in function.keys():
        print("\n(1) Buy")
        print("(2) Remove Item")
        print("(3) Edit Quantity")
        print("(x) Back")
        action = input().upper()

    return function[action]()

def buy():
    for name, value in __main__.userCart.items():
        if not products.get(name):
            print(f"Item {name} does not exist anymore!")
            showCart()
            return
        
        if value > products[name]["quantity"]:
            print(f'There is not enough quantity of {name}, there are only {products[name]["quantity"]} left!')
            showCart()
            return
        
    total = 0
    for name, value in __main__.userCart.items():
        products[name]["quantity"] -= value
        total += products[name]['price'] * value

    order = {
        "name": __main__.currentUser,
        "order": __main__.userCart,
        "price": total
    }
    
    admin.newOrder(order)

    __main__.userCart = {}
    
    print("Thanks for buying at DJ Shop! Come back again!")
    userMenu()
    return
        

def addToCart():
    user = __main__.currentUser

    names = list(products.keys())
    for i, x in enumerate(names):
        print(f"{i}) {x}")
    
    index = int(input("Index of product to add: "))

    qt = int(input("Quantity to add: "))
    
    item = names[index]

    if qt < 0 or qt > products[item]["quantity"]:
        print("Invalid quantity!\n")
        userMenu()
        return
    

    if not __main__.userCart.get(item):
        __main__.userCart[item] = 0

    __main__.userCart[item] += qt

    autenti.saveCart(__main__.currentUser)
    
    print("Successfully added")

    print()
    userMenu()