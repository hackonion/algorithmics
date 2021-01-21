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
    scores = set()
    second_lower = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.add(score)
    
    lower = sorted(scores)[1]
    
    for name, score in students:
        if score == lower:
            second_lower.append(name)
    
    for name in sorted(second_lower):
        print(name, end="\n")