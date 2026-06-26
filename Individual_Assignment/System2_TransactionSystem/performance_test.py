import time

from binary_search import binary_search, linear_search



def performance_test(transactions):


    search_id = "T010"


    print("\nPerformance Testing")
    print("--------------------")


    start = time.time()


    binary_search(
        transactions,
        search_id,
        0,
        len(transactions)-1
    )


    binary_time = time.time() - start



    start = time.time()


    linear_search(
        transactions,
        search_id
    )


    linear_time = time.time() - start



    print("Binary Search Time:",
          binary_time,
          "seconds")


    print("Linear Search Time:",
          linear_time,
          "seconds")