def binary_search(arr, item):
    n = len(arr)

    left = 0
    right = n - 1
    found_index = -1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == item:
            found_index = mid
            break
        elif arr[mid] > item:
            left = mid + 1
        else:
            right = mid - 1

    return found_index



def binary_sort(arr):
    n = len(arr)

    for i in range(n):
        new_i = binary_search(arr[:i+1], arr[i])
        while i > 0 and i != new_i:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

from random import choices
a = list(choices(range(1, 100), k=10))
binary_sort(a)
print(a)
