import math
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1

    count = [0] * range_size
    output = [0] * len(arr)

    # Подсчёт элементов
    for num in arr:
        count[num - min_val] += 1

    # Кумулятивный подсчёт
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Построение выходного массива
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

# В зависимости от того сколько элементов в массиве и какой из них самый большой могут применяться следующие сортировки:
# Если сумма длинны массива и его макс элемента не слишком велика, и в нем нет дробных данных используется counting_sort
# Если длинна массива умноженная на кол-во разрядов его максимального элемента не слишком велика, используется radix_sort
# Если же оба значения выше больше чем n*log(n) то используется heap_sort с гарантированным временем n*log(n) и потреблением памяти O(1)
def manager(arr):
    n = len(arr)
    max_num = max(max(arr),abs(min(arr)))
    d = len(str(max_num))

    if min(n+max_num, n*d, n*math.log(n)) == n+max_num and any(not isinstance(item, int) for item in arr) == False:
        print("Используется counting_sort")
        return counting_sort(arr)

    elif min(n+max_num, n*d, n*math.log(n)) == n*d:
        print("Используется radix_sort")
        return radix_sort(arr)

    else:
        print("Используется heap_sort")
        return heap_sort(arr)

arr = [1,10,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0.9]
print(manager(arr))