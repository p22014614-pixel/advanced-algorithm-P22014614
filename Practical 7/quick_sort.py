def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # choose last element as pivot
    left = []
    right = []

    for x in arr[:-1]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [214, 12, 46, 57, 31, 8]
sorted_arr = quick_sort(arr)

print("Quick Sorted array: ", arr)