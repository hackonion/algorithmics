#https://leetcode.com/problems/find-all-duplicates-in-an-array/
""" 
    Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
    and each integer appears once or twice, return an array of all the integers that appears twice.

    You must write an algorithm that runs in O(n) time and uses only constant extra space.
    
"""

from typing import DefaultDict, List


def findDuplicates(nums: List[int]) -> List[int]:
        dic = DefaultDict(int)
        result = []
        
        if nums is None or len(nums) <= 1:
            return []
        for i in nums:
            dic[i] += 1
    
        for i in dic:
        
            if dic[i] >= 2:
                result.append(i)
        result.sort()
        return result

nums = [4,3,2,7,8,2,3,1]

findDuplicates(nums)