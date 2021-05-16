#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""
    Given head which is a reference node to a singly-linked list. 
    The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

    Return the decimal value of the number in the linked list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: ListNode) -> int:
        
    string = "0b"
    while head is not None:
            
        string = string + str(head.val)
            
        head = head.next
        
    result = int(string,2)
    return result
