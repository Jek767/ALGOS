#56. Merge Intervals
# Функция сортирует массив по возрастанию, после чего циклом проходит все его элементы если интервалы накладываются друг на друга
# то их обЪединяют если конец второго больше конца первого, а если второй входит в первый то он его поглощает
# Cложность - O(n^2*log(n))
def merge(intervals: list[list[int]]) -> list[list[int]]:
    if len(list) == 0:
        return -1
    intervals.sort(key=lambda x: x[0])
    lst = []
    for start, end in intervals:
        if not lst or lst[-1][1] < start:
            lst.append([start, end])
        else:
            lst[-1][1] = max(lst[-1][1], end)
    return lst

list = [[-2,-1],[1,3],[2,6],[8,10],[15,18],[0,2],[10,12],[0,100]]
print(merge(list))