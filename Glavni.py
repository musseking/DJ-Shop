currentUser = None

def register():
    with open("login.txt", "r") as lg:
        Username = input("Create username: ")
        Password = input("Create password: ")

        for i in lg:
            if not '|' in i:
                continue

            if Username == i.split("|")[0].strip():
                print("Korisnicko ime je zauzeto!")
                return
            

    with open("login.txt", "a") as lg:
        lg.write(Username + "|" + Password + "\n")

    currentUser = Username
    print("Successful registration!")

    
def login():
    user = input("Username: ")
    passw = input("Password: ")
    with open("login.txt", "r") as f:

        for line in f.readlines():
            if not '|' in line:
                continue
            us, pw = line.split("|")
            pw = pw.strip()

            if (user == us) and (passw == pw):
                print ("Login successful!")
                currentUser = us
                return
    
    print("Wrong username/password")

def menu():

    functions = {
        "1": login,
        "2": register,
        "X": exit
    }

    action = None
    while not action in functions.keys():
        print("(1) Sign in")
        print("(2) Sign up")
        print("(X) Exit")
        action  = input().upper()

    functions[action]()

def main():
    print("\nRecords of employees\n")
    
    while (1 < 2):
        menu()
     

if __name__ == '__main__':
    main()