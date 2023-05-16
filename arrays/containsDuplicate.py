#!/usr/bin/env python3

def containsDuplicate(nums):
    refMap = {}

    for i in range(len(nums)):
        if nums[i] in refMap:
            return True
        else:
            refMap[nums[i]] = True

    return False

print(containsDuplicate([1,2,3,1]))
