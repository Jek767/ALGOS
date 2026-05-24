def longestConsecutive(nums: list[int]) -> int:
    nums = set(nums)
    nums = sorted(nums)
    count = 1
    list_count = []
    if len(nums)==0:
        return 0
    for i in range(0,len(nums)-1):
        if nums[i]+1 == nums[i+1]:
            count += 1
        else:
            list_count.append(count)
            count = 1
    list_count.append(count)
    return max(list_count)