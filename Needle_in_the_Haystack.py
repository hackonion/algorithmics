# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
"""
    Can you find the needle in the haystack?

    Write a function findNeedle() that takes an array full of junk but containing one "needle"

    After your function finds the needle it should return a message (as a string) that says:

    "found the needle at position " plus the index it found the needle, so:

    find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
"""

def find_needle(haystack):
    
    for index,value in enumerate(haystack):
        if value == 'needle':
            return print(index)


find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])