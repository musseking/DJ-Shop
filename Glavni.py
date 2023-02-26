#import Oprema
#import Radnici
#import Korisnik

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
    logged = False
    with open("login.txt", "r") as f:

        for line in f.readlines():
            us, pw = line.split("|")
            pw = pw.replace('\n', '')

            if (user == us) and (passw == pw):
                print ("Login successful!")
                logged = True
                break

    if logged:
        print("Logged in successfully!")
        currentUser = us
        return
    
    print("Wrong username/password")

def menu():
    print("dome")

def main():
    print()
    print("Records of employees")
    print()
    #register()
    login()
     

if __name__ == '__main__':
    main()