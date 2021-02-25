# https://leetcode.com/problems/reverse-integer/
"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

def reverse(x: int) -> int:
    rev_x = int(str(abs(x))[::-1])
    if rev_x == 0: return 0
    
    if rev_x.bit_length() > 31:
        return 0
    else:
        if x < 0 :            
            return rev_x
        else:
            return rev_x
        
                        
reverse(123)
