#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""
    Given an array nums of n integers where nums[i] is in the range [1, n],
    return an array of all the integers in the range [1, n] that do not appear in nums.
"""

from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
        
        arr = []
        size = len(nums) + 1
        nums = set(nums)
        for i in range(1,size):
            
            if i not in nums:
                arr.append(i)
            
        return arr

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))