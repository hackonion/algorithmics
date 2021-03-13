#https://leetcode.com/problems/palindrome-number/
"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
"""
def isPalindrome(x: int):
    x_string = str(x)
    x_reverse = x_string[::-1]
    
    if x_string == x_reverse:
        return True
    else:
        return False
    


print(isPalindrome(-101))