def insert_sort(arr):
    n = len(arr)

    for ind in range(n):

        i = ind
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


from random import choices

a = list(choices(range(1, 100), k=10))
insert_sort(a)
print(a)