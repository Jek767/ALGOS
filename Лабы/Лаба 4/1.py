#Сумма двух
def twoSum(nums: list[int], target: int) -> list[int]:
    dict = {}
    for i in range(0,len(nums)):
        dict[nums[i]] = i
    for i in range(0,len(nums)):
        minus = target - nums[i]
        if minus in dict and dict[minus]!=i:
            return [i,dict[minus]]

print(twoSum([2,7,11,15],9))