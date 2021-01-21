# https://leetcode.com/problems/search-insert-position/
"""
    Given a sorted array of distinct integers and a target value,
    return the index if the target is found. If not, return the index where it would be if it were inserted in order.
    
    Example 1:

    Input: nums = [1,3,5,6], target = 5
    Output: 2
"""

from typing import List


nums = [1,3,5,6]

target = 2

def searchInsert(nums: List[int], target: int) -> int:
    
    
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        if  target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
    


searchInsert(nums,target)