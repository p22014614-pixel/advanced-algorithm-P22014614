import threading
import time

from factorial import factorial



results = {}



def calculate_factorial(number):

    start = time.time_ns()


    result = factorial(number)


    end = time.time_ns()


    results[number] = result



def run_multithreading():

    start_time = time.time_ns()


    thread1 = threading.Thread(
        target=calculate_factorial,
        args=(50,)
    )


    thread2 = threading.Thread(
        target=calculate_factorial,
        args=(100,)
    )


    thread3 = threading.Thread(
        target=calculate_factorial,
        args=(200,)
    )



    thread1.start()
    thread2.start()
    thread3.start()



    thread1.join()
    thread2.join()
    thread3.join()



    end_time = time.time_ns()


    total_time = end_time - start_time


    return total_time



def multithreading_experiment():

    total = 0


    print("\nMultithreading Experiment")


    for i in range(10):

        time_taken = run_multithreading()


        print(
            "Round",
            i+1,
            ":",
            time_taken,
            "nanoseconds"
        )


        total += time_taken



    average = total / 10


    print(
        "\nAverage Time:",
        average,
        "nanoseconds"
    )