def shaker_sort(arr):
    n = len(arr)

    l = 0
    r = n - 1
    swapped = True

    while swapped:
        swapped = False
        for i in range(l, r):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        r -= 1

        if not swapped:
            break

        for i in range(r, l, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        l += 1
