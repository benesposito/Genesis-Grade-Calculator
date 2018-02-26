import re

file = open("D:\\Code\\Python\\PyCharm\\GradeCalculator.txt", "r")
regex = re.compile(r"(\d+\.?\d*)\s\/\s(\d+\.?\d*)")

grades = []

for line in file:
    occurence = regex.search(line)

    if occurence != None:
        grades.append(regex.search(line))

num = 0
den = 0

for grade in grades:
    num += float(grade.group(1))
    den += float(grade.group(2))

print(num / den)