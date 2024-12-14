def shell_sort(arr):
    n = len(arr)
    distance = n - 1

    while distance:
            for start in range(distance, n):
                i = start
                while i > 0 and arr[i] < arr[i - distance]:
                    arr[i], arr[i - distance] = arr[i - distance], arr[i]
                    i -= distance
            distance //= 2

from random import choices
a = list(choices(range(1, 100), k=10))
shell_sort(a)
print(a)