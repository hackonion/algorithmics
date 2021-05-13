#https://leetcode.com/problems/squares-of-a-sorted-array/
"""
    Given an integer array nums sorted in non-decreasing order,
    return an array of the squares of each number sorted in non-decreasing order.
"""

from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    
    for num in range(len(nums)):
        nums[num] = pow(nums[num],2)
    
    return sorted(nums)
            
nums = [-4,-1,0,3,10]

print(sortedSquares(nums))
