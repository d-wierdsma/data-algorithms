#!/usr/bin/env python3

def rotate(nums, k):
    if k == 0:
        return nums
    
    k = k % len(nums)
    
    nums = nums[len(nums)-k:] + nums[:len(nums)-k]

    return nums

print(rotate([1,2,3,4,5,6,7], 3))
