# https://leetcode.com/problems/reverse-string/solution/
"""
    Write a function that reverses a string. The input string is given as an array of characters char[].

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.
"""
def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(l,r):
            if l < r:
                s[l],s[r] = s[r],s[l]
                swap(l+1,r-1)
        swap(0,len(s)-1)
        print(s)
            
            
    
    

hola = ['h','o','l','a']
reverseString(hola)
    