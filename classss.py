class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, customer ID: {self.customer_id}, Phone: {self.phone}"


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, product ID: {self.product_id}"


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"{self.product}, Quantity: {self.quantity}"

    def get_total_price(self):
        return self.product.price * self.quantity


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def __str__(self):
        return f"order id: {self.order_id}, {self.customer}"

    def add_item(self, product, quantity):
        for i in self.items:
            if i.product == product:
                i.quantity += quantity
                return
        order_item = OrderItem(product, quantity)
        self.items.append(order_item)

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.get_total_price()
        return total_price


class OrderManagementSystem:
    def __init__(self):
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

    def remove_order(self, password, order_id):
        if password == 1:
            if order_id not in self.orders:
                raise ValueError("Invalid order_id")
            del self.orders[order_id]


store = OrderManagementSystem()
lst_names = ["Emma", "Noah", "Olivia", "Liam", "Ava", "William", "Sophia", "Mason", "Isabella", "James", "Mia", "Benjamin", "Charlotte", "Jacob", "Amelia", "Michael", "Harper", "Elijah", "Evelyn", "Ethan", "Abigail", "Alexander", "Emily", "Daniel", "Elizabeth", "Matthew", "Mila", "Aiden", "Ella", "Henry"]
lst_products = ['T-shirt', 'Jeans', 'Sneakers', 'Watch', 'Sunglasses', 'Perfume', 'Handbag', 'Backpack', 'Jacket', 'Hoodie', 'Sweater', 'Skirt', 'Dress', 'High heels', 'Running shoes', 'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Bluetooth speaker', 'Gaming console', 'Camera', 'Fitness tracker', 'Smartwatch', 'Virtual reality headset', 'Drone', 'Wireless earbuds', 'Fitness equipment', 'Electric razor', 'Air purifier']
lst_phone_numbers = ["1234567890", "9876543210", "5555555555", "1111111111", "9999999999", "4444444444", "8888888888", "6666666666", "7777777777", "2222222222", "3333333333", "5551234567", "8885559999", "1112223333", "4445556666", "7778889999", "1231231234", "4564564567", "7897897890", "3213213210", "6546546540", "8881234567", "5555551212", "9879879870", "3334445555", "6667778888", "1112223334", "4445556667", "7778889990", "1231231235", "4564564568"]
lst_email = ["emma@example.com", "noah@example.com", "olivia@example.com", "liam@example.com", "ava@example.com", "william@example.com", "sophia@example.com", "mason@example.com", "isabella@example.com", "james@example.com", "mia@example.com", "benjamin@example.com", "charlotte@example.com", "jacob@example.com", "amelia@example.com", "michael@example.com", "harper@example.com", "elijah@example.com", "evelyn@example.com", "ethan@example.com", "abigail@example.com", "alexander@example.com", "emily@example.com", "daniel@example.com", "elizabeth@example.com", "matthew@example.com", "mila@example.com", "aiden@example.com", "ella@example.com", "henry@example.com"]
lst_price = [20.0, 50.0, 80.0, 200.0, 100.0, 60.0, 150.0, 70.0, 120.0, 50.0, 80.0, 40.0, 100.0, 90.0, 100.0, 800.0, 1200.0, 500.0, 150.0, 100.0, 400.0, 600.0, 80.0, 300.0, 500.0, 1000.0, 120.0, 500.0, 50.0, 300.0]
for i in range(30):
    store.add_customer(i, lst_names[i], lst_email[i], lst_phone_numbers[i])
    store.add_product(i, lst_products[i], lst_price[i])

# for i in range(30):
#     print(store.customers[i])
#
# for i in range(30):
#     print(store.products[i])
