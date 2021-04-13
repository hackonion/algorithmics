#https://leetcode.com/problems/fibonacci-number/
"""
    The Fibonacci numbers, commonly denoted F(n) form a sequence,
    called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
"""

#Recursion solution
from typing import Counter


def fib(n: int) -> int:
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

#Usin a Iterative  
def fib_for(n:int) -> int:
    
    prev = 1
    curr = 0
    for i in range(0,n):
        curr = curr + prev
        prev = curr - prev
    
    return curr
        
    

test = 3
print(fib_for(test))