recursive_count = 0


def merge_sort(arr):

    global recursive_count

    # Divide step
    if len(arr) > 1:

        recursive_count += 1

        middle = len(arr)//2

        left_half = arr[:middle]
        right_half = arr[middle:]


        # Conquer step
        merge_sort(left_half)
        merge_sort(right_half)


        # Combine step
        merge(arr, left_half, right_half)



def merge(arr, left, right):

    i = 0
    j = 0
    k = 0


    # Compare and combine two sorted halves
    while i < len(left) and j < len(right):

        if left[i].transactionID < right[j].transactionID:

            arr[k] = left[i]
            i += 1

        else:

            arr[k] = right[j]
            j += 1


        k += 1



    # Copy remaining left elements

    while i < len(left):

        arr[k] = left[i]
        i += 1
        k += 1



    # Copy remaining right elements

    while j < len(right):

        arr[k] = right[j]
        j += 1
        k += 1