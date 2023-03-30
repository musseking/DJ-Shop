import matplotlib.pyplot as plt
import admin

def allSales():
    sales = {}
    for order in admin.orders:
        for name, value in order["order"].items():
            if not sales.get(name):
                sales[name] = 0
            sales[name] += value

    plt.clf()
    plt.title("All item sales")
    plt.bar(list(sales.keys()), list(sales.values()))
    plt.xlabel("Item names")
    plt.ylabel("Item sales")
    plt.show()

def userSales(user):
    sales = {}
    for order in admin.orders:
        if user == order["name"]:
            for name, value in order["order"].items():
                if not sales.get(name):
                    sales[name] = 0
                sales[name] += value

    plt.clf()
    plt.title(f"Item purchases by {user}")
    plt.bar(list(sales.keys()), list(sales.values()))
    plt.xlabel("Item names")
    plt.ylabel("Item sales")
    plt.show()


