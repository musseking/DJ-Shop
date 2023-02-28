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

    print("Successful registration!\n")
    return Username

    
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
                print ("\nLogin successful!\n")
                return us
    
    print("\nWrong username/password\n")

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

    return functions[action]()