# Technology Assessment
# Alejandra Trejo Rodriguez

import retail
import unittest


class TestRetail(unittest.TestCase):

    def setUp(self):
        # Set up store
        self.test_store = retail.Store("Test Store")
        # Add items to store
        self.test_store.add_item("apples", 2.0, "grocery")
        self.test_store.add_item("pen", 1.0, "non-grocery")
        self.test_store.add_item("notebook", 5.0, "non-grocery")

    def test_employee(self):
        employee_cashier = retail.Cashier()
        customer_type = "employee"
        employee_cashier.add_to_bag("apples", 50)
        employee_cashier.add_to_bag("pen", 50)
        employee_cashier.add_to_bag("notebook", 50)
        total = employee_cashier.calculate_bill(self.test_store, customer_type)
        self.assertEqual(total, 295)

    def test_affiliate(self):
        affiliate_cashier = retail.Cashier()
        customer_type = "affiliate"
        affiliate_cashier.add_to_bag("apples", 50)
        affiliate_cashier.add_to_bag("pen", 50)
        affiliate_cashier.add_to_bag("notebook", 50)
        total = affiliate_cashier.calculate_bill(self.test_store, customer_type)
        self.assertEqual(total, 355)

    def test_two_year(self):
        two_year_cashier = retail.Cashier()
        customer_type = "2_year_customer"
        two_year_cashier.add_to_bag("apples", 50)
        two_year_cashier.add_to_bag("pen", 50)
        two_year_cashier.add_to_bag("notebook", 50)
        total = two_year_cashier.calculate_bill(self.test_store, customer_type)
        self.assertEqual(total, 370)

    def test_no_discount(self):
        other_customer_cashier = retail.Cashier()
        customer_type = "other"
        other_customer_cashier.add_to_bag("apples", 50)
        other_customer_cashier.add_to_bag("pen", 50)
        other_customer_cashier.add_to_bag("notebook", 50)
        total = other_customer_cashier.calculate_bill(self.test_store, customer_type)
        self.assertEqual(total, 380)


if __name__ == '__main__':
    unittest.main()