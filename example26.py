def read_file(file_name):
    with open(f'{file_name}.txt') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.replace("\n", "").split("\t")
    return lines

diabetes_data = read_file("diabetes_data")

count = 0
total = 0
for i in range(1, len(diabetes_data)):
    if int(diabetes_data[i][4]) > 55 and diabetes_data[i][3] != "NA":
        total += float(diabetes_data[i][3])
        count += 1

average = total / count
print(average)