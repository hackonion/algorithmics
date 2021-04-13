#https://leetcode.com/problems/majority-element/
"""
    Given an array nums of size n, return the majority element.
    
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array
"""

from collections import Counter
from typing import List

#Implement dict
def map_cout(num:List[int]):
    num_map = Counter(num)   
    return max(num_map,key=num_map.get)
 
test = [2,3,4,5,6,6,3,4,56,6]
print(map_cout(test))