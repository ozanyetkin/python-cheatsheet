def read_file(file_name):
    with open(f'{file_name}.txt') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.replace("\n", "").split("\t")
    return lines
"""
count = 0
total = 0
for i in range(1, len(diabetes_data)):
    if int(diabetes_data[i][4]) > 55 and diabetes_data[i][3] != "NA":
        total += float(diabetes_data[i][3])
        count += 1

average = total / count
print(average)
"""
def gen_dict(file_name):
    data = read_file(file_name)
    column_num = len(data[0])
    dictionary = {}
    for i in range(column_num):
        sutun = []
        for j in range(1, len(data)):
            sutun.append(data[j][i])
        dictionary.update({data[0][i]: sutun})
    return dictionary


def find_na(dicti):
    dicti_na = {}
    for key in dicti.keys():
        count_key = 0
        for val in dicti[key]:
            if val == "NA":
                count_key += 1
        dicti_na.update({key: count_key})
    return dicti_na

def find_min_max(lookup, minim, maxim, target, dicti):
    target_min = 99999
    target_max = 0
    for i, val in enumerate(dicti[lookup]):
        if val != "NA" and dicti[target][i] != "NA":
            if maxim >= float(val) >= minim:
                if float(dicti[target][i]) < target_min:
                    target_min = float(dicti[target][i])
                if float(dicti[target][i]) > target_max:
                    target_max = float(dicti[target][i])
    return (target_min, target_max)

def filter_dict(lookup, minim, maxim, dicti):
    f_dict = dicti.copy()

    for key in f_dict.keys():
        f_dict.update({key: []})
    
    for i, val in enumerate(dicti[lookup]):
        if val != "NA":
            if maxim >= float(val) >= minim:
                for key in f_dict.keys():
                    f_dict[key].append(dicti[key][i])
    return f_dict

if __name__ == "__main__":
    diabetes_data = read_file("diabetes_data")
    diabetes_dict = gen_dict("diabetes_data")
    filtered = filter_dict("Age", 26, 28, diabetes_dict)
    print(diabetes_dict.keys())
    print(find_na(diabetes_dict))
    print(find_min_max("Age", 20, 30, "blood_pressure", diabetes_dict))
    print(find_min_max("Age", 20, 30, "serum_insulin", diabetes_dict))
    print(find_min_max("serum_insulin", 20, 50, "Age", diabetes_dict))
    print(filtered)
