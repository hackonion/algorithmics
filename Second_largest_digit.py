#https://leetcode.com/problems/second-largest-digit-in-a-string/
"""
    Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

    An alphanumeric string is a string consisting of lowercase English letters and digits.

"""


def secondHighest(s: str) -> int:
    
    nums = []
    
    for i in s:
        if i.isdigit():
            if i not in nums:
                nums.append(i)
    nums.sort()
    print(nums)
    if len(nums) < 2:
        return -1
    
    return nums[-2]
            
    
s = "co077"
print(secondHighest(s))


nums = [1,2,3,4,5,6]
