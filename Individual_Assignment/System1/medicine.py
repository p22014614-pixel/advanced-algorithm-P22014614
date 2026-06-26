class Medicine:
    def __init__(self, medicine_id, name, category, price, quantity):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display(self):
        print("--------------------------------")
        print("Medicine ID:", self.medicine_id)
        print("Name:", self.name)
        print("Category:", self.category)
        print("Price: RM", self.price)
        print("Quantity:", self.quantity)