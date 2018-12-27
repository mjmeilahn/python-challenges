#!/bin/python3

import os
import sys

def gradingStudents(grades):
    if len(grades) <= 60:
        filtered = filter(lambda grade : grade >= 0, grades)
        output = []

        for grade in filtered:
            if grade >= 38:
                if grade % 5 == 3:
                    grade += 2
                elif grade % 5 == 4:
                    grade += 1

            output.append(grade)

        return output

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
