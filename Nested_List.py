# https://www.hackerrank.com/challenges/nested-list/problem
"""
    Given the names and grades for each student in a class of

    students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

    Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

    Example
    The ordered list of scores is , so the second lowest score is . There are two students with that score:

    . Ordered alphabetically, the names are printed as:

    alpha
    bet
"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    

    new = []
    ordened_list = sorted(students,key=lambda x:x[1])
    new = ordened_list[1:3][:]
    new.sort(key=lambda x:x[0])


    for index,i in enumerate(new):
        print(i[:][0])