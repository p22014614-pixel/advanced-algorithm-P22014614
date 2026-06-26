from transaction import Transaction

from merge_sort import merge_sort, recursive_count

from binary_search import binary_search, linear_search

from performance_test import performance_test


transactions = [

Transaction("T015","Alice","Laptop",3500,"10-05-2026"),

Transaction("T003","David","Mouse",80,"12-05-2026"),

Transaction("T009","Sarah","Phone",2500,"15-05-2026"),

Transaction("T001","John","Keyboard",150,"20-05-2026"),

Transaction("T012","Mary","Tablet",900,"22-05-2026"),

Transaction("T005","Peter","Headphone",300,"25-05-2026"),

Transaction("T010","Kevin","Monitor",800,"28-05-2026"),

Transaction("T002","Amy","Camera",1200,"30-05-2026"),

Transaction("T014","Jason","Printer",600,"01-06-2026"),

Transaction("T007","Linda","Smart Watch",500,"05-06-2026"),

Transaction("T011","Chris","Speaker",250,"07-06-2026"),

Transaction("T006","Emma","Phone Case",50,"10-06-2026"),

Transaction("T013","Ryan","USB Cable",30,"12-06-2026"),

Transaction("T004","Sophia","Power Bank",100,"15-06-2026"),

Transaction("T008","Daniel","Tablet Pen",70,"18-06-2026")

]



def display_all():

    print("\nALL TRANSACTIONS")

    for transaction in transactions:

        transaction.display()



while True:


    print("\n==============================")
    print(" Online Shopping Transaction System")
    print("==============================")

    print("1. Display Transactions")
    print("2. Sort using Merge Sort")
    print("3. Search using Binary Search")
    print("4. Search using Linear Search")
    print("5. Performance Test")
    print("6. Exit")


    choice=input("Enter choice: ")



    if choice=="1":

        display_all()



    elif choice=="2":

        print("\nBefore Sorting")

        display_all()


        merge_sort(transactions)


        print("\nAfter Sorting")

        display_all()


        print(
            "\nRecursive calls:",
            recursive_count
        )



    elif choice=="3":

        key=input("Enter Transaction ID: ")


        result=binary_search(
            transactions,
            key,
            0,
            len(transactions)-1
        )


        if result:

            print("Transaction Found")
            result.display()

        else:

            print("Transaction Not Found")



    elif choice=="4":

        key=input("Enter Transaction ID: ")


        result=linear_search(
            transactions,
            key
        )


        if result:

            print("Transaction Found")
            result.display()

        else:

            print("Transaction Not Found")



    elif choice=="5":

        performance_test(transactions)



    elif choice=="6":

        print("System Closed")
        break



    else:

        print("Invalid Choice")