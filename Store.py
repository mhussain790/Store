# 3 classes - Product, Customer, and Store
# All data members are privata and accessed through get/set methods

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

    # SET METHODS
    def set_product_id(self, new_id):
        self._product_id = new_id

    def set_title(self, new_title):
        self._title = new_title

    def set_description(self, new_description):
        self._description = new_description

    def set_price(self, new_price):
        self._price = new_price

    def set_quantity_available(self, new_quantity_avail):
        self._quantity_available = new_quantity_avail

    # Decrease quantity available by one
    def decrease_quantity(self):
        if self._quantity_available > 0:
            self._quantity_available -= 1


class Customer:

    def __init__(self, name, customer_id, premium_member: bool):
        self._name = name
        self._customer_id = customer_id
        self._premium_member = premium_member
        self.customer_cart = []

    # initialize an empty list for hold product ID codes for customer cart
    # customer_cart = []

    # A private collection (list, dictionary, etc) of Product ID codes with a get method
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
        self.customer_cart.append(new_product)

    # empty customer cart
    def empty_cart(self):
        self.customer_cart.clear()


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

    # def lookup_product_from_id(self, product_id):
    #     for item in self.inventory:
    #         if item.get_product_id() == product_id:
    #             return product_id
    #         else:
    #             return None

    # TODO: RETURN PRODUCT
    def lookup_product_from_id(self, product_id):
        for item in range(len(self._inventory)):
            if self._inventory[item].get_product_id() == product_id:
                return self._inventory[item]
            else:
                return None

    # TODO: RETURN MEMBER
    def lookup_member_from_id(self, customer_id):
        for member in self._membership:
            if customer_id == member.get_customer_id():
                return str(member.get_name())
            else:
                return None

    #
    # def product_search(self, search_string):
    #     # Initialize empty list to store case insensitive products
    #     sorted_list = []
    #
    #     # Sort through inventory to find the matching product
    #     for item in range(len(self.inventory)):
    #         for word in self.inventory[item].get_title().split():
    #             if search_string.lower() == word.lower():
    #                 sorted_list.append(word)
    #         break
    #
    #     # Sort unordered list
    #     sorted_list.sort()
    #
    #     # Return empty sorted list
    #     return sorted_list

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
        for item in self._inventory:
            if product_id == item.get_product_id():
                print("Product found " + item.get_title())

                for member in self._membership:
                    if customer_id == member.get_customer_id():
                        print("Member ID found")

                        if item.get_quantity_available() > 0:
                            member.add_product_to_cart(item)
                            print("Product added to cart!")

                        else:
                            print("Product out of stock!")

                    elif item not in self._membership:
                        print("Member ID NOT found")
            elif item not in self._inventory:
                print("Product not found")

    # TODO: FINISH METHOD
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
                        print("Total cost for premium member is " + str(total_cost))
                    else:
                        shipping_cost = cost_of_products * 0.07
                        total_cost = cost_of_products + shipping_cost
                        print("Total cost is " + str(total_cost))
                else:
                    raise InvalidCheckoutError

        except InvalidCheckoutError:
            print("ERROR: There was an issue checking out!")


# TODO: MAIN METHOD
# TODO: UNIT TEST

prod = Product(1001, "mango", "i like mangos", 35, 0)
prod_2 = Product(1002, "orange", "juicy orange", 45, 300)
prod_3 = Product(1003, "apple", "green apple", 55, 400)
prod_4 = Product(1004, "MANGO", "large mango", 65, 100)
cust = Customer("dani", 3534, False)
# testing_inv = [1, 2, 3, 4, 5, 1001]
# member_list = [444, 2494,3092392, 3534]
# new = Store(prod,cust)
# print(new.inventory)

myStore = Store()
myStore.add_product(prod)
myStore.add_product(prod_2)
myStore.add_product(prod_3)
myStore.add_product(prod_4)
myStore.add_member(cust)
# print(myStore.inventory[0].get_product_id())
# print(myStore.membership[0].get_customer_id())
print(myStore.lookup_product_from_id(1001))
print(myStore.lookup_member_from_id(3534))
# print(myStore.product_search("mango"))
#
# print(myStore.add_product_to_member_cart(1003, 3534))

print(myStore.check_out_member(354))
