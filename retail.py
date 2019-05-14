# Technology Assessment
# Alejandra Trejo Rodriguez


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.grocery_items = []
        self.non_grocery = []

    def add_item(self, item_name, item_price, item_category):
        if item_category == "grocery":
            self.grocery_items.append(Item(item_name, item_price))
        else:
            self.non_grocery.append(Item(item_name, item_price))

    def list_items(self):
        for product in self.grocery_items:
            print(product)
        for product in self.non_grocery:
            print(product)




class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return "{}\t{}".format(self.name, self.price)


def main():
    # Set up store
    mck_store = Store("McKinsey Store")

    # Add items to store
    mck_store.add_item("Mandarins", 4.5, "grocery")
    mck_store.add_item("Apples", 2.0, "grocery")
    mck_store.add_item("Cheese", 5.5, "grocery")
    mck_store.add_item("Chocolates", 10.75, "grocery")
    mck_store.add_item("Salt", 1.0, "grocery")
    mck_store.add_item("Detergent", 22.5, "non-grocery")
    mck_store.add_item("Toilet paper", 16.25, "non-grocery")
    mck_store.add_item("Pen", 1.0, "non-grocery")
    mck_store.add_item("Notebook", 5.0, "non-grocery")
    mck_store.add_item("Mop", 34.5, "non-grocery")

    # List items
    mck_store.list_items()


if __name__ == '__main__':
    main()
