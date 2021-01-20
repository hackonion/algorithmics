# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

"""
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format
The first line contains a string consisting of space separated words.

Output Format
Print the formatted string as explained above.

Sample Input

this is a string   

Sample Output

this-is-a-string
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format
The first line contains a string consisting of space separated words.

Output Format
Print the formatted string as explained above.

Sample Input

this is a string   

Sample Output

this-is-a-string
 
"""

def split_and_join(line:str):
    line = line.split(" ")
    line = "-".join(line)
    return line
    
split_and_join("this is a string")