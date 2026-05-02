#88. Merge Sorted Array
# Функция проходит по nums1 и nums2, если число из nums1 меньше или равно чем число из nums2 и следующие число меньше или равно, то
# Число вписывают в nums1, удаляют из nums2, из nums1 удаляется 0 с конца и цикл переходит к следующиму элементу nums1
# В конце, когда остаются только нули, числа вписываются вместо них
# Переменная s используетя для определения когда начнутся незначащие нули
# Несморя на два цикла сложность - O(n+m)
def merge( nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        n = len(nums1)
        if n == 0 or len(nums2)==0:
            return "Один из списков пуст"
        s=0
        for i in range(0, n):
            for j in nums2:
                if nums2 and nums1[i] <= j and ( n>i+1 and nums1[i + 1] >= j):
                    nums1.insert(i + 1, j)
                    nums1.pop(-1)
                    nums2.pop(0)
                    s+=1
                    break

                elif nums2 and nums1[i] > j:
                    nums1.insert(i, j)
                    nums1.pop(-1)
                    nums2.pop(0)
                    s+=1
                    break

                elif i>= m+n:
                    nums1.insert(i, j)
                    nums1.pop(-1)
                    nums2.pop(0)
                    break
                else:
                    break

nums1 = [-1,0,0,0,3,0,0,0,0,0,0]
m = 5
nums2 = [-1,-1,0,0,1,2]
n = 6
merge(nums1,m,nums2,n)
print(nums1)