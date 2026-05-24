def topKFrequent(nums: list[int], k: int) -> list[int]:
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    if k>len(dict):
        return False
    list_count = sorted(dict.items(),key = lambda item: item[1])
    result = []
    for i in range(len(list_count)-1,len(list_count)-k-1,-1):
        result.append(list_count[i][0])
    return result

print(topKFrequent([1,2,1,2,1,2,3,1,3,2],2))

