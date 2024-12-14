def hairbrush_sort(arr):
    print(id(arr))
    factor_reduction = 1.247
    n = len(arr)

    distance = int(n // factor_reduction)
    swapped = True
    while swapped:

        swapped = False
        for i in range(distance, n):
            if arr[i - distance] > arr[i]:
                arr[i - distance], arr[i] = arr[i], arr[i - distance]
                swapped = True

        if distance < factor_reduction:
            distance = 1
        else:
            distance = int(distance // factor_reduction)

print(hairbrush_sort.__name__)

# from random import choices
#
# a = list(choices(range(1, 100), k=10))
# hairbrush_sort(a)
# print(a)
