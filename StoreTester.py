from Store import Product, Customer, Store
import unittest


class TestStore(unittest.TestCase):
    """"
    Contains unit tests for Product, Customer, and Store functions
    """

    def test_1(self):
        first_product = Product(1, "Lemon", "Fresh lemons", 3, 10)
        first_customer = Customer("Mohammad", 31343, True)
        first_store = Store()

        test_bool = first_customer.is_premium_member()
        self.assertTrue(test_bool)

    def test_2(self):
        second_test_product_1 = Product(121, "Banana", "Yellow Banana", 2.50, 10)
        second_test_product_2 = Product(220, "Mango", "Tropical Mango", 4, 5)
        second_test_product_3 = Product(5778, "Doritos", "Cool Ranch Doritos", 3.99, 3)
        second_test_customer = Customer("Rondo", 778304, False)
        second_store = Store()

        # Add Customer to store
        second_store.add_member(second_test_customer)

        # Add products to cart
        second_store.add_product(second_test_product_1)
        second_store.add_product(second_test_product_2)
        second_store.add_product(second_test_product_3)

        total_price = second_store.check_out_member(778304)
        self.assertAlmostEqual(total_price, 11.2243)

    def test_3(self):
        third_test_customer_1 = Customer("FIRST CUSTOMER", 12345, True)
        third_test_customer_2 = Customer("SECOND CUSTOMER", 23456, False)
        third_test_customer_3 = Customer("THIRD CUSTOMER", 34567, False)

        third_store = Store()

        third_store.add_member(third_test_customer_1)
        third_store.add_member(third_test_customer_2)
        third_store.add_member(third_test_customer_3)

        test_3 = third_store.lookup_member_from_id(23456)
        self.assertIs(test_3, "SECOND CUSTOMER")

    def test_4(self):
        fourth_product = Product(200, "Pencil", "Number 2 Pencil", 0.99, 1)
        product_price = fourth_product.get_price()

        self.assertEqual(product_price, 0.99)

    def test_5(self):
        fifth_test_customer = Customer("Robot", 3000, True)

        fifth_test_product_1 = Product(2345, "Box of Apples", "Box of six green apples", 1, 1)

        fifth_store = Store()

        fifth_store.add_member(fifth_test_customer)
        fifth_store.add_product(fifth_test_product_1)

        result = fifth_store.add_product_to_member_cart(2345, 3000)

        self.assertEqual(result, "Product added to cart")


if __name__ == '__main__':
    unittest.main()