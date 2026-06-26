def binary_search(arr, target, low, high):

    # Base condition
    if low <= high:

        middle = (low + high)//2


        # Found transaction
        if arr[middle].transactionID == target:

            return arr[middle]


        # Search right side

        elif arr[middle].transactionID < target:

            return binary_search(
                arr,
                target,
                middle + 1,
                high
            )


        # Search left side

        else:

            return binary_search(
                arr,
                target,
                low,
                middle - 1
            )


    return None



def linear_search(arr, target):

    for transaction in arr:

        if transaction.transactionID == target:

            return transaction


    return None