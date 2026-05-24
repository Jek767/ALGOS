#С использованием словаря
# def containsDuplicate(nums: list[int]) -> bool:
#     dict = {}
#     for i in nums:
#         if i in dict:
#             return True
#         else:
#             dict[i] = 0
#     return False

#Наиболее быстрый
def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

print(containsDuplicate([1,2,3,1,5]))