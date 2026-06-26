class Transaction:

    def __init__(self, transactionID, customerName, productName, amount, transactionDate):
        self.transactionID = transactionID
        self.customerName = customerName
        self.productName = productName
        self.amount = amount
        self.transactionDate = transactionDate


    def display(self):
        print("--------------------------------")
        print("Transaction ID:", self.transactionID)
        print("Customer Name:", self.customerName)
        print("Product Name:", self.productName)
        print("Amount: RM", self.amount)
        print("Transaction Date:", self.transactionDate)