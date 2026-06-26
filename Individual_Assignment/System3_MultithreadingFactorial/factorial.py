def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result



def repeated_factorial(number, repeat):

    result = None

    for i in range(repeat):

        result = factorial(number)

    return result