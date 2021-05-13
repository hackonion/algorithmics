#https://leetcode.com/problems/valid-parentheses/
"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    1-. Open brackets must be closed by the same type of brackets.
    2-. Open brackets must be closed in the correct order.
"""

def isValid(s: str) -> bool:
    map_string = {"}":"{","]":"[",")":"("}
    stack = []
    
    for item in s:        
        if item in map_string:
            top = stack.pop() if stack else "#"
            if stack != None:
                if map_string[item] != top:
                    return False       
        else:
            stack.append(item)                
            
    return not stack




