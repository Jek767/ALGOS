def firstMissingPositive(nums: list[int]) -> int:
    dict = {}
    for i in nums:
        dict[i]=0
    for i in range(1,1000000000000):
        if not i in dict:
            return i






print(firstMissingPositive([100000, 3, 4000, 2, 15,  99999]))
