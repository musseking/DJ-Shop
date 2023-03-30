import autenti, __main__, json

import products, graphs

with open("orders.json", "r") as f:
    orders = json.load(f)

def newOrder(order):
    orders.append(order)
    with open("orders.json", "w") as f:
        json.dump(orders, f)

    with open("products.json", "w") as f:
        json.dump(products.products, f)
    
    with open(f"carts/{__main__.currentUser}.json", "w") as f:
        json.dump({}, f)

def addProduct():
    productName = input("Product name (Type 'none' to go back): ")
    if productName == "none":
        print()
        adminMenu()
        return
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

def editQuantity():
    for name, values in products.products.items():
        print(f'Name: {name:30}', f'Brand: {values["brand"]:30}', f'Price: {values["price"]:13.2f} RSD', f'Quantity: {values["quantity"]:7}', sep="\t")

    names = list(products.products.keys())
    for i, x in enumerate(names):
        print(f"{i}) {x}")
    
    index = int(input("Index of product to edit quantity: "))
    qt = int(input("Enter new quantity: "))
    
    item = names[index]

    if qt < 0:
        print("Invalid quantity!\n")
        adminMenu()
        return
    
    products.products[item]["quantity"] = qt

    with open("products.json", "w") as f:
        json.dump(products.products, f)
    
    print("Successfully edited quantity!\n")
    adminMenu()

def removeItem():
    for name, values in products.products.items():
        print(f'Name: {name:30}', f'Brand: {values["brand"]:30}', f'Price: {values["price"]:13.2f} RSD', f'Quantity: {values["quantity"]:7}', sep="\t")

    names = list(products.products.keys())
    for i, x in enumerate(names):
        print(f"{i}) {x}")
    
    index = int(input("Index of product to edit quantity: "))
    
    item = names[index]
    
    del products.products[item]

    with open("products.json", "w") as f:
        json.dump(products.products, f)
    
    print("Successfully deleted!\n")
    adminMenu()



def listProducts():

    functions = {
        "1": showAll,
        "2": search,
        "3": back1,
        "X": exit
    }
    option = None
    while not option in functions.keys():
        print("(1) Show all products")
        print("(2) Search")
        print("(3) Back")
        option = input().upper()

    return functions[option]()

def back1():
    adminMenu()

def logout():
    __main__.currentUser = None
    __main__.main()

def allSales():
    graphs.allSales()
    adminMenu()

def userSales():
    user = input("Enter username: ")
    graphs.userSales(user)
    adminMenu()

def adminMenu():
    functions = {
        "1": addProduct,
        "2": editQuantity,
        "3": removeItem,
        "4": listProducts,
        "5": orderList,
        "6": allSales,
        "7": userSales,
        "8": logout,
        "X": exit
    }

    action = None
    while not action in functions.keys():
        print("(1) Add a product")
        print("(2) Edit quantity")
        print("(3) Remove product")
        print("(4) List of products")
        print("(5) Order list")
        print("(6) Graph of all sales")
        print("(7) Graph of sales by user")
        print("(8) Log out")
        print("(X) Exit")
        action  = input().upper()

    functions[action]()

def orderList():
    for index, order in enumerate(orders):
        print(f'Order ID: {index}')
        print(f'Buyer: {order["name"]}')
        
        for name, value in order["order"].items():
            print(f'Item: {name:30}', f'Quantity: {value:7}', sep="\t")

        print(f'Total price: {order["price"]}')
        print()
    
    input("Press 'Enter' to continue! ")

    adminMenu()

def showAll():
    for name, values in products.products.items():
        print(f'Name: {name:30}', f'Brand: {values["brand"]:30}', f'Price: {values["price"]:13.2f} RSD', f'Quantity: {values["quantity"]:7}', sep="\t")

    print()
    input("Press 'Enter' to continue! ")
    adminMenu()

def search():
    term = input("Search: ").lower()
    for name, values in products.products.items():
        if term in name.lower():
            print(f'Name: {name:30}', f'Brand: {values["brand"]:30}', f'Price: {values["price"]:13.2f} RSD', f'Quantity: {values["quantity"]:7}', sep="\t")

    print()
    input("Press 'Enter' to continue! ")
    adminMenu()