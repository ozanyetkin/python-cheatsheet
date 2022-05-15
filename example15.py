with open('grades.txt') as f:
    lines = f.readlines()
"""
for i in range(len(lines)):
    lines[i]
"""
name_list = []
grade_list = []
for line in lines:
    line = line.replace("\n", "").replace(" ", "")
    name_list.append(line.split(",")[0])
    grade_list.append(int(line.split(",")[1]))

"""
    name = ""
    grade = ""
    for i, char in enumerate(line):
        if i < line.find(","):
            name += char
        elif char == ",":
            pass
        else:
            grade += char
    print(name)
    print(grade)
"""

sum = 0
for grade in grade_list:
    sum += grade
average = sum / len(grade_list)
print(average)

"""
for i, grade in enumerate(grade_list):
    name_list[i]
"""

for name, grade in zip(name_list, grade_list):
    if float(grade) > average:
        print(f"{name} sinavdan {grade} almistir ve {average} olan ortalamanin uzerindedir")
    else:
        print(f"{name} sinavdan {grade} almistir ve {average} olan ortalamanin altindadir")
