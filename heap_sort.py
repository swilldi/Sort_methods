type numeric_array = List[int | float]
class Heap:
    __heap_data: numeric_array
    __heap_size: int
    __count_swaps: int

    def __init__(self, arr_source):
        # создаем кучу, добавляя в нее каждый элемент массива
        self.__heap_size = 0
        self.__count_swaps = 0
        max_elem = max(arr_source)
        self.__heap_data = [max_elem + 1] * len(arr_source)
        for elem in arr_source:
            self.insert(elem)

    def __swap(self, ind, jind):
        self.__heap_data[ind], self.__heap_data[jind] = self.__heap_data[jind], self.__heap_data[ind]
        self.__count_swaps += 1

    # Перестраиваем кучу, если элемент ind увеличился. Меняем местами i-ый элемент с наименьшим из его сыновей и выполняем для сына ту же процедуру
    # Время работы О(h), i.e O(logn)
    def __sift_down(self, ind):
        while 2 * ind + 1 < self.__heap_size:
            left = 2 * ind + 1
            right = 2 * ind + 2
            jind = left
            if right < self.__heap_size and self.__heap_data[right] < self.__heap_data[left]:
                jind = right
            if self.__heap_data[ind] <= self.__heap_data[jind]:
                break
            self.__swap(ind, jind)
            ind = jind

    # Перестраиваем кучу, если элемент ind уменьшился. Проталкиваем маленькие элементы наверх, меняя их местами с родителем
    # Время работы О(h), i.e O(logn)
    def __sift_up(self, ind):
        while ind - 1 >= 0 and self.__heap_data[ind] < self.__heap_data[(ind - 1) // 2]:
            half_ind = (ind - 1) // 2
            self.__swap(ind, half_ind)
            ind = half_ind

    # Вставляем элемент в кучу и проталкиваем его наверх, восстанавливая инвариант кучи
    def insert(self, key):
        self.__heap_data[self.__heap_size] = key
        self.__heap_size += 1
        self.__sift_up(self.__heap_size - 1)

    # По инварианту кучи минимальный элемент - корень. Удаляем его и перестраиваем кучу
    def extract_min(self):
        cur_min = self.__heap_data[0]
        self.__heap_data[0] = self.__heap_data[-1]
        self.__heap_size -= 1
        self.__heap_data.pop()
        self.__sift_down(0)
        return cur_min

    # Сортирует переданный массив и возвращает количество перестановок
    def sort_array(self, arr_to_sort):
        self.__count_swaps = 0
        size = len(arr_to_sort)
        for i in range(size):
            arr_to_sort[i] = self.extract_min()
        return self.__count_swaps
