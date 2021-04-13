# 3 classes - Product, Customer, and Store
# All data members are private and accessed through get/set methods

class Product:

    def __init__(self, product_id, title, description, price, quantity_available):
        self._product_id = product_id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    # GET METHODS
    def get_product_id(self):
        return self._product_id

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def get_quantity_available(self):
        return self._quantity_available

    # Decrease quantity available by one
    def decrease_quantity(self):
        if self._quantity_available > 0:
            self._quantity_available -= 1


class Customer:

    def __init__(self, name, customer_id, premium_member: bool):
        self._name = name
        self._customer_id = customer_id
        self._premium_member = premium_member
        self._customer_cart = []

    # A private collection (list, dictionary, etc) of Product ID codes with a get method
    def get_customer_cart(self):
        return self._customer_cart

    def get_name(self):
        return self._name

    def get_customer_id(self):
        return self._customer_id

    # Method that returns whether customer is premium member (True/False)
    def is_premium_member(self):
        if self._premium_member is True:
            return True
        else:
            return False

    # add product ID code to customer's cart
    def add_product_to_cart(self, new_product):
        self._customer_cart.append(new_product)

    # empty customer cart
    def empty_cart(self):
        self._customer_cart.clear()


class InvalidCheckoutError(Exception):
    pass


class Store:

    def __init__(self):
        self._inventory = []
        self._membership = []

    def add_product(self, new_product):
        self._inventory.append(new_product)

    def add_member(self, new_customer):
        self._membership.append(new_customer)

    def lookup_product_from_id(self, product_id):
        found = False
        for products in self._inventory:
            if product_id == products.get_product_id():
                return products.get_title()
                found = True
        if not found:
            return None

    def lookup_member_from_id(self, customer_id):
        found = False
        for member in self._membership:
            if customer_id == member.get_customer_id():
                return member.get_name()
                found = True
        if not found:
            return None

    def product_search(self, search_string):
        # Initialize empty list to store case insensitive products
        sorted_list = []

        # Sort through inventory to find the matching product
        for item in self._inventory:
            for word in item.get_title().split():
                for chunks in item.get_description():
                    if search_string.lower() == word.lower() or search_string.lower() == chunks.lower():
                        sorted_list.append(word)
                        print("word is " + word)
                    break
            break

        # Sort unordered list
        sorted_list.sort()

        # Return empty sorted list
        return sorted_list

    def add_product_to_member_cart(self, product_id, customer_id):

        for item, member in zip(self._inventory, self._membership):
            if product_id != item.get_product_id():
                return "Product ID not found"
            elif customer_id != member.get_customer_id():
                return "Member ID not found"
            elif item.get_quantity_available() > 0:
                member.add_product_to_cart(item)
                return "Product added to cart"
            else:
                return "Product out of stock"

    def check_out_member(self, customer_id):
        try:
            cost_of_products = 0
            shipping_cost = 0

            for member in self._membership:
                if customer_id == member.get_customer_id():
                    for products in self._inventory:
                        if products.get_quantity_available() > 0:
                            cost_of_products += products.get_price()
                            products.decrease_quantity()
                    if member.is_premium_member() is True:
                        total_cost = cost_of_products + shipping_cost
                        return total_cost
                    else:
                        shipping_cost = cost_of_products * 0.07
                        total_cost = cost_of_products + shipping_cost
                        return total_cost
                else:
                    raise InvalidCheckoutError

        except InvalidCheckoutError:
            return "ERROR: There was an issue checking out!"


def main():
    my_store = Store()
    prod = Product(1001, "mango", "tropical very nice mangos", 35, 10)
    prod_2 = Product(1002, "orange", "juicy orange", 45, 2)
    prod_3 = Product(1003, "apple", "green apple", 55, 1)
    prod_4 = Product(1004, "MANGO", "large mango", 65, 3)
    cust = Customer("test", 3534, False)

    my_store.add_product(prod)
    my_store.add_product(prod_2)
    my_store.add_product(prod_3)
    my_store.add_product(prod_4)
    my_store.add_member(cust)

    return my_store.check_out_member(3534)


if __name__ == '__main__':
    main()