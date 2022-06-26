products = {
    "T": "Top",
    "H": "Hoodie",
    "B": "Backpack"
}

while True:
    key = input()

    if key == "-1":
        break
    else:
        print(products[key])
