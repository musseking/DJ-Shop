import auth, products, admin

currentUser = None

def main():
    global currentUser
    while not currentUser:
        currentUser = auth.menu()
    if currentUser == "admin":
        admin.adminMenu()
    else:
        products.userMenu()
    

if __name__ == '__main__':
    print("\nWelcome to DJ Shop!")
    print("Created by Vasilije Medić\n")

    main()