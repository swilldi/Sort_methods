def gnome_sort(arr):
    n = len(arr)

    i = 0
    while i != n - 1:
        if arr[i + 1] < arr[i]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            if i > 0:
                i -= 1
        else:
            i += 1

from random import choices
a = list(choices(range(1, 100), k=10))
gnome_sort(a)
print(a)

