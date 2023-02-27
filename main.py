import auth, shop

def main():
    print("\nWelcome to DJ Shop!")
    print("Created by Vasilije Medić\n")

    currentUser = None

    while not currentUser:
        currentUser = auth.menu()
    shop.menu()
     

if __name__ == '__main__':
    main()