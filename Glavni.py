currentUser = None

def register():
    with open("login.txt", "r") as lg:
        Username = input("Create username: ")
        Password = input("Create password: ")

        korisnickoIme = []
        sifre = []

        for i in lg:
            if not '|' in i:
                continue

            a, b = i.split("|")
            b = b.strip()

            korisnickoIme.append(a)
            sifre.append(b)
            
    data = dict(zip(korisnickoIme, sifre))
    print(data)

    with open("login.txt", "a") as lg:
        lg.write(Username + "|" + Password + "\n")

    currentUser = korisnickoIme
    print("Successful registration!")

    
def login():
    user = input("Username: ")
    passw = input("Password: ")
    with open("login.txt", "r") as f:

        for line in f.readlines():
            us, pw = line.split("|")
            pw = pw.replace('\n', '')

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
        print("(1) Prijavite se")
        print("(2) Registrujte se")
        print("(X) Izadjite")
        action  = input().upper()

    functions[action]()

def main():
    print("\nRecords of employees\n")
    
    menu()
     

if __name__ == '__main__':
    main()