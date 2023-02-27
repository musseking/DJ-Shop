def addProduct():
    productName = input("Product name: ")
    productBrand = input("Product brand: ")
    productPrice = float(input("Product price: "))
    productQuantity = int(input("Product quantity: "))

    with open("products.txt", "a") as prod:
        prod.write(productName + "|" + productBrand + "|" + str(productPrice) + "|" + str(productQuantity) + "\n")

def deleteProduct():
    pass

def listProducts():
    pass

def back():
    pass

def menu():

    functions = {
        "1": addProduct,
        "2": deleteProduct,
        "3": listProducts,
        "4": back,
        "X": exit
    }

    action = None
    while not action in functions.keys():
        print("(1) Add a product")
        print("(2) Remove product")
        print("(3) List of products")
        print("(4) Back")
        print("(X) Exit")
        action  = input().upper()

    functions[action]()