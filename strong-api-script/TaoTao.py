def extend(nums: list[int],enlarge: int)-> list[int]:
    res = 0 * (len(nums) + enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res

