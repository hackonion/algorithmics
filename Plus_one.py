# https://leetcode.com/problems/plus-one/

""" 
    Given a non-empty array of decimal digits representing a non-negative integer,

    increment one to the integer.The digits are stored such that the most significant 

    digit is at the head of the list, and each element in the array contains a single digit.

    You may assume the integer does not contain any leading zero, except the number 0 itself.

    Example 1:

    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.

"""

from typing import List

digits = [1,2,3]

def plusOne(digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            digits[i] +=1
            if digits[i] < 10:
                return print(digits)
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits.insert(0,1)
        return print(digits)

plusOne(digits)