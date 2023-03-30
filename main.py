import autenti, admin, products
currentUser = None
userCart = {}

def main():
    global currentUser, userCart
    while not currentUser:
        currentUser = autenti.menu()

    userCart = autenti.getCart(currentUser)

    if currentUser == "admin":
        admin.adminMenu()
    else:
        products.userMenu()


if __name__ == '__main__':
    print("\nWelcome to DJ Shop!")
    print("Created by Vasilije Medić\n")

    main()