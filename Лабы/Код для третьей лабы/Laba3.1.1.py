#912. Sort an Array
#Решение с использованием Heap Sort, сложность - O(n*log(n))
#Функция проходит по бинарному дереву перемещая большие числа вверх а маленькие вниз от i-ого элемента до элемента с индексом upper
def heapify(arr, i, upper):
    while(True):
        l, r = i * 2 + 1, i * 2 + 2
        if max(l,r)<upper:
            if arr[i] >= max(arr[l],arr[r]):
                break
            elif arr[l]>arr[r]:
                arr[i],arr[l] = arr[l],arr[i]
                i = l
            else:
                arr[i], arr[r] = arr[r], arr[i]
                i = r
        elif l < upper:
            if arr[l]>arr[i]:
                arr[i],arr[l] = arr[l],arr[i]
                i = l
            else:
                break
        elif r < upper:
            if arr[r] > arr[i]:
                arr[i], arr[r] = arr[r], arr[i]
                i = r
            else:
                break
        else:
            break

def heap_sort(arr):
    #В цикле проходим по тем элементам которые имеют дочернии в бинарном дереве
    for i in range((len(arr)-2)//2,-1,-1):
        heapify(arr, i, len(arr))

    #В цикле проходим по всем элементам выводя наибольший неотсортированный элемент вверх(индекс[0]) и меняем его местами с последним неотсортированным элементом
    for end in range(len(arr)-1,0,-1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr,0,end)
    return arr

list = [5,16,8,14,20,1,26]

print(heap_sort(list))
