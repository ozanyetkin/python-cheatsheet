class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.shopping_list = []

    def add_item(self, item):
        self.shopping_list += item
    
    def get_balance(self):
        self.balance = 0
        for item in self.shopping_list:
            self.balance += item.get_balance()
        return self.balance


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_balance(self):
        return self.price

c1 = Cart("ozan")
c2 = Cart("bundle")

i1 = Item("mouse", 79.90)
i2 = Item("keyboard", 129.90)

c2.add_item([i1, i2])
c1.add_item([c2, i1])

print(c1.owner)
print(c1.shopping_list)

c1.get_balance()

print(c1.balance)