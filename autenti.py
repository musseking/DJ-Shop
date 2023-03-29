import __main__

import json
from hashlib import sha256

with open("login.json", "r") as lg:
    users = json.load(lg)

def getCart(user):
    try:   
        with open(f"carts/{user}.json", "r", encoding="utf8") as f:
            return json.load(f)
    except:
        return {}
    
def saveCart(user):
    with open(f"carts/{user}.json", "w", encoding="utf8") as f:
        json.dump(__main__.userCart, f)


def register():
    global Username
    Username = input("Create username: ")
    Password = input("Create password: ").encode("utf-8")

    if users.get(Username):
        print("User already exists")
    users[Username] = sha256(Password).hexdigest()

    with open("login.json", "w", encoding="utf8") as lg:
        json.dump(users, lg)

    print("Successful registration!\n")
    with open (f"{Username}.json", "w") as f:
        print("Your cart has been created successfully!")
    
    
    return Username
    

    
    

def login():
    user = input("Username: ")
    passw = input("Password: ").encode("utf-8")
    if users.get(user) == sha256(passw).hexdigest():
        print("Logged in successfully\n")

        return user
    
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