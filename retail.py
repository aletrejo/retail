# Technology Assessment
# Alejandra Trejo Rodriguez

import pprint
import math


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

    def exists(self, item):
        for each in self.grocery_items:
            if each.name == item:
                return True
        for each in self.non_grocery:
            if each.name == item:
                return True
        return False

    def is_grocery(self, item):
        for grocery in self.grocery_items:
            if grocery.name == item:
                return True
        return False

    def find_item(self, item):
        for each in self.grocery_items:
            if each.name == item:
                return each
        for each in self.non_grocery:
            if each.name == item:
                return each


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return "{}\t{}".format(self.name, self.price)


class Cashier:
    def __init__(self):
        self.shopping_cart = {}

    def create_shopping_bag(self):
        new_item = True
        while new_item:
            item_name = input("Please enter the name of the item. If you're done adding items to your cart, enter done: ")
            if item_name == 'done':
                new_item = False
            else:
                price = input("Quantity: ")
                self.add_to_bag(item_name.strip(), int(price))

    def add_to_bag(self, item, quantity):
        if item not in self.shopping_cart:
            self.shopping_cart[item] = quantity
        else:
            print("Item already exists in shopping cart.")

    def display_bag(self):
        print("====== YOUR SHOPPING LIST ======")
        pprint.pprint(self.shopping_cart)

    def calculate_bill(self, store, customer_type):
        total = 0
        discount = self.get_percentage_discount(customer_type)

        # Iterate over each item in shopping list
        for item, quantity in self.shopping_cart.items():
            if store.exists(item):
                if store.is_grocery(item):
                    # Grocery item == no percentage discount
                    total += quantity * store.find_item(item).price

                else:
                    total += quantity * store.find_item(item).price * discount
            else:
                continue

        # Add discount per hundred
        #print('After percentage discount: {}'.format(total))
        hundreds = math.floor(total / 100)
        price_off = 5 * hundreds
        total = total - price_off
        #print('After hundreds discount {}'.format(total))
        return total



    def get_percentage_discount(self, customer_type):
        if customer_type == "2_year_customer":
            return .95
        elif customer_type == "employee":
            return .7
        elif customer_type == "affiliate":
            return .9
        else:
            return 1


def main():
    # Set up store
    mck_store = Store("McKinsey Store")

    # Add items to store
    mck_store.add_item("mandarins", 4.5, "grocery")
    mck_store.add_item("apples", 2.0, "grocery")
    mck_store.add_item("cheese", 5.5, "grocery")
    mck_store.add_item("chocolates", 10.75, "grocery")
    mck_store.add_item("salt", 1.0, "grocery")
    mck_store.add_item("detergent", 22.5, "non-grocery")
    mck_store.add_item("toilet paper", 16.25, "non-grocery")
    mck_store.add_item("pen", 1.0, "non-grocery")
    mck_store.add_item("notebook", 5.0, "non-grocery")
    mck_store.add_item("mop", 34.5, "non-grocery")

    # List items
    print("====== STORE ITEMS ======")
    mck_store.list_items()

    # Open store for operations
    store_open = True

    while store_open:
        # Greet customer and create a new cashier for each customer
        current_cashier = Cashier()
        print("Welcome to {}'s checkout system!".format(mck_store.store_name))

        # Determine customer type
        customer_type = input("Please enter the customer type ('employee', 'affiliate', '2_year_customer'): ")
        if customer_type not in ['employee', 'affiliate', '2_year_customer']:
            customer_type = 'other'

        # Add items to their shopping bag
        current_cashier.create_shopping_bag()
        current_cashier.display_bag()
        print("====== YOUR TOTAL ======")
        total_bill = current_cashier.calculate_bill(mck_store, customer_type)
        print("Your total to pay is: {} ".format(total_bill))

        # Process a new customer or exit
        new_customer = input("Is there another customer waiting in the line? (Y/N) ")
        new_customer = new_customer.upper()
        if new_customer == 'N':
            store_open = False


if __name__ == '__main__':
    main()
