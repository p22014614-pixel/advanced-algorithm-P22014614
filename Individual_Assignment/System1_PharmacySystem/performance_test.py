import time
from medicine import Medicine
from hashTable import HashTable


def linear_search(medicine_list, medicine_id):
    for medicine in medicine_list:
        if medicine.medicine_id == medicine_id:
            return medicine
    return None


def performance_test():
    print("\n===== Hash Table Search Performance Test =====")

    medicine_list = []
    hash_table = HashTable(50)

    sample_data = [
        Medicine("M001", "Panadol", "Tablet", 5.50, 100),
        Medicine("M002", "Cough Syrup", "Syrup", 12.00, 50),
        Medicine("M003", "Vitamin C", "Supplement", 20.00, 80),
        Medicine("M004", "Antibiotic", "Tablet", 15.00, 30),
        Medicine("M005", "Eye Drop", "Liquid", 8.00, 40),
        Medicine("M006", "Flu Tablet", "Tablet", 10.00, 60),
        Medicine("M007", "Calcium", "Supplement", 18.00, 70),
        Medicine("M008", "Bandage", "First Aid", 3.00, 120),
        Medicine("M009", "Antiseptic", "Liquid", 9.50, 35),
        Medicine("M010", "Allergy Tablet", "Tablet", 13.00, 45)
    ]

    for medicine in sample_data:
        medicine_list.append(medicine)
        hash_table.insert(medicine)

    search_id = "M010"

    start = time.time_ns()
    hash_result = hash_table.search(search_id)
    hash_time = time.time_ns() - start

    start = time.time_ns()
    linear_result = linear_search(medicine_list, search_id)
    linear_time = time.time_ns() - start

    print("\nSearching for Medicine ID:", search_id)

    print("\nHash Table Search Result:")
    if hash_result:
        hash_result.display()
    else:
        print("Medicine not found")

    print("\nLinear Search Result:")
    if linear_result:
        linear_result.display()
    else:
        print("Medicine not found")

    print("\nPerformance Result")
    print("------------------")
    print("Hash Table Search Time:", hash_time, "nanoseconds")
    print("Linear Search Time:", linear_time, "nanoseconds")