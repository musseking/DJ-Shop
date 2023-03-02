import auth, admin, usermenu

def main():
   

    currentUser = None

    while not currentUser:
        currentUser = auth.menu()
    if currentUser == "admin":
        admin.adminMenu()
    else:
        usermenu.userMenu()
    

if __name__ == '__main__':
    print("\nWelcome to DJ Shop!")
    print("Created by Vasilije Medić\n")

    main()