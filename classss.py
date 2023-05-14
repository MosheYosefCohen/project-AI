import random
class Customer:
    def _init_(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone


class Product:
    def _init_(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class OrderItem:
    def _init_(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity


class Order:
    def _init_(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def add_item(self, product, quantity):
        order_item = OrderItem(product, quantity)
        self.items.append(order_item)

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.get_total_price()
        return total_price


class OrderManagementSystem:
    def _init_(self):
        self.customers = {}
        self.products = {}
        self.orders = {}

    def add_customer(self, customer_id, name, email, phone):
        customer = Customer(customer_id, name, email, phone)
        self.customers[customer_id] = customer

    def add_product(self, product_id, name, price):
        product = Product(product_id, name, price)
        self.products[product_id] = product

    def create_order(self, order_id, customer_id):
        if customer_id not in self.customers:
            raise ValueError("Invalid customer_id")
        customer = self.customers[customer_id]
        order = Order(order_id, customer)
        self.orders[order_id] = order
        return order

    def add_item_to_order(self, order_id, product_id, quantity):
        if order_id not in self.orders:
            raise ValueError("Invalid order_id")
        if product_id not in self.products:
            raise ValueError("Invalid product_id")
        product = self.products[product_id]
        order = self.orders[order_id]
        order.add_item(product, quantity)

    def get_order_total(self, order_id):
        if order_id not in self.orders:
            raise ValueError("Invalid order_id")
        order = self.orders[order_id]
        return order.get_total_price()

lis_of_names = ["Emma", "Noah", "Olivia", "Liam", "Ava", "William", "Sophia", "Mason", "Isabella", "James", "Mia", "Benjamin", "Charlotte", "Jacob", "Amelia", "Michael", "Harper", "Elijah", "Evelyn", "Ethan", "Abigail", "Alexander", "Emily", "Daniel", "Elizabeth", "Matthew", "Mila", "Aiden", "Ella", "Henry"]
lis_of_names = ['T-shirt', 'Jeans', 'Sneakers', 'Watch', 'Sunglasses', 'Perfume', 'Handbag', 'Backpack', 'Jacket', 'Hoodie', 'Sweater', 'Skirt', 'Dress', 'High heels', 'Running shoes', 'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Bluetooth speaker', 'Gaming console', 'Camera', 'Fitness tracker', 'Smartwatch', 'Virtual reality headset', 'Drone', 'Wireless earbuds', 'Fitness equipment', 'Electric razor', 'Air purifier']
