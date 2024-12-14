# надо без доп массивов
def quick_sort(arr, reverse=None):
    from random import randint

    n = len(arr)
    if n < 2:
        return arr

    # определяем опорное число
    pivot_ind = randint(0, n - 1)
    pivot = arr[pivot_ind]

    # списки левых, правых и равных чисел
    left = []
    middle = [pivot]
    right = []

    for i in range(n):
        if i == pivot_ind:
            continue

        el = arr[i]
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            middle.append(el)

    if reverse is None:
        return quick_sort(left) + middle + quick_sort(right)
    else:
        return quick_sort(right) + middle + quick_sort(left)

