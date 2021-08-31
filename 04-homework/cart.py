class Cart:
    def __init__(self, items=[], total=0):
        self.items = items
        self.total = total

    def additem(self, item):
        self.items.append(item)

    def removeitem(self, item, price, quantity):
        if quantity >= self.items[item]:

            self.total -= (self.items[item] * price)
            self.items.pop(item, None)
        else:
            self.items[item] -= quantity
            self.total -= (quantity * price)

    def view(self):
        v = set(self.items)
        for items in v:
            print(f'{items}, [{self.items.count(items)}]')
        print(f'${self.total:,.2f}')
        
        def __repr__(self): 
            return(self.items)


class Item:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

    def addprice(self, price):
        self.total += price

    def addquantity(self, quantity):
        self.items += quantity


cart1 = Cart()

while True:
    choice = input(""""This is your shopping cart.
Type 'add' to add an item to your cart.
Type 'remove' to remove an item from your cart.
Type 'view' to view your cart. 
Type 'quit' to exit""")

    if choice == 'add':
        add = input("What would you like to add to your cart?")
        q = input("How many of these items do you want?")
        p = input("what is the price of this Item?")

        new_product = Item(add, int(q), float(p))
        cart1.additem(new_product)

    elif choice == 'remove':
        cart1.view()
        remove = input("What would you like to remove from your cart? ")
        remprice = input("What was the price of this item? ")
        remquant = input("How much of this item did you have? ")
        #cart1.removeitem(remove, int(remquant)(remove, float(remprice)))

    elif choice == 'view':
        cart1.view()
        continue

    elif choice == 'quit':
        cart1.view()
        break

    else:
        continue
