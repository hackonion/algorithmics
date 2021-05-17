#https://leetcode.com/problems/sum-of-unique-elements/
""" 
    You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

    Return the sum of all the unique elements of nums.
"""

from collections import defaultdict
from typing import List

def sumOfUnique(nums: List[int]) -> int:
    
    unique = defaultdict(int)
    result = 0
    
    for num in nums:
        unique[num] += 1
    
    
    for i in unique:
        
        if unique[i] == 1:
            result += i
            
    return result
        
        
        
    

    
    

nums = [1,1,1,1,1,1]
sumOfUnique(nums)