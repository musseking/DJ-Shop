def showCart():
    with open("usercart.txt", "r") as f:
        for i, line in enumerate(f):
            print("{0}) {1}".format(i+1, line))