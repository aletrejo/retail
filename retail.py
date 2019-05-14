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

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


def main():
    pass


if __name__ == '__main__':
    main()
