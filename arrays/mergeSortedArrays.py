#!/usr/bin/env python3

def mergeSortedArrays(arr1, arr2):
    totalItems = len(arr1) + len(arr2)
    arr1Index = 0
    arr2Index = 0
    result = []

    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    for i in range(totalItems):
        if arr2Index >= len(arr2) or arr1[arr1Index] < arr2[arr2Index]:
            result.append(arr1[arr1Index])
            arr1Index += 1
        else:
            result.append(arr2[arr2Index])
            arr2Index += 1

    return result





print(mergeSortedArrays([0,3,4,31], []))
