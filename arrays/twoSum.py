#!/usr/bin/env python3

def twoSum(nums, target):
    refMap = {}

    if len(nums) < 2:
        return []

    for i in range(len(nums)):
        if (target - nums[i]) in refMap:
            return [refMap[target - nums[i]], i]
        elif nums[i] in refMap:
            continue
        else:
            refMap[nums[i]] = i

    return []

print(twoSum([2,2,4], 6))
