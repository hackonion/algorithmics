#https://leetcode.com/problems/minimum-distance-to-the-target-element/
"""
    Given an integer array nums (0-indexed) and two integers target and start,
    find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

    Return abs(i - start).

    It is guaranteed that target exists in nums.

"""


from typing import List


def getMinDistance(nums: List[int], target: int, start: int) -> int:
        
        mini = float('inf')
        for key, item in enumerate(nums):
            
            if item == target:
                mini = min(abs(key - start),mini)
                return mini

nums = [1,2,3,4,5]
target = 5
start = 3
print(getMinDistance(nums,target,start))