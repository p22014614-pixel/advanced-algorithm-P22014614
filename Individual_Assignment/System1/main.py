from medicine import Medicine
from hashTable import HashTable


inventory = HashTable(20)



# Sample records

sample_data = [

    Medicine("M001", "Panadol", "Tablet", 5.50, 100),

    Medicine("M002", "Cough Syrup", "Syrup", 12.00, 50),

    Medicine("M003", "Vitamin C", "Supplement", 20.00, 80),

    Medicine("M004", "Antibiotic", "Tablet", 15.00, 30),

]


for medicine in sample_data:
    inventory.insert(medicine)



while True:

    print("\n===== Pharmacy Inventory System =====")
    print("1. Display Inventory")
    print("2. Insert Medicine")
    print("3. Search Medicine")
    print("4. Exit")


    choice = input("Enter choice: ")


    if choice == "1":

        inventory.display()



    elif choice == "2":

        id = input("Medicine ID: ")
        name = input("Medicine Name: ")
        category = input("Category: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))


        new_medicine = Medicine(
            id,
            name,
            category,
            price,
            quantity
        )


        inventory.insert(new_medicine)



    elif choice == "3":

        id = input("Enter Medicine ID: ")

        result = inventory.search(id)


        if result:

            print("Medicine Found:")
            result.display()

        else:

            print("Medicine not found")



    elif choice == "4":

        print("System Closed")
        break


    else:

        print("Invalid choice")