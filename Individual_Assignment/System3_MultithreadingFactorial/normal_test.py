import time

from factorial import factorial



def run_normal():

    start_time = time.time_ns()



    factorial(50)

    factorial(100)

    factorial(200)



    end_time = time.time_ns()


    return end_time - start_time





def normal_experiment():

    total = 0


    print("\nNormal Execution Experiment")



    for i in range(10):


        time_taken = run_normal()


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