import json
from hashlib import sha256

with open("login.json", "r") as lg:
    users = json.load(lg)

def register():
    
    Username = input("Create username: ")
    Password = input("Create password: ").encode("utf-8")

    if users.get(Username):
        print("User already exists")
        return
    users[Username] = sha256(Password).hexdigest()

    with open("login.json", "w", encoding="utf8") as lg:
        json.dump(users, lg)

    print("Successful registration!\n")
    return Username

def login():
    user = input("Username: ")
    passw = input("Password: ").encode("utf-8")
    if users.get(user) == sha256(passw).hexdigest():
        print("Logged in successfully")
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