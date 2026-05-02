#75. Sort Colors
#Для сортировки без применения дополнительных массивов используется Heap Sort
# Сложность - O(n*log(n))
class Solution:
    @staticmethod
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
            Solution.heapify(arr, n, largest)

    @staticmethod
    def sortColors(arr: list[int]) -> None:
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            Solution.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            Solution.heapify(arr, i, 0)


nums = [2, 0, 2, 1, 1, 0,0,0,0]
Solution.sortColors(nums)  # теперь работает
print(nums)


