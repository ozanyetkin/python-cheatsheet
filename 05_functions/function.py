def my_function():
    print("function is called")

def square_root(a_number):
    square_rooted = a_number ** (1/2)
    return square_rooted

# print(square_root(16))
# print(square_root(8))

def calculate_average(a_list):
    sum = 0
    for a_num in a_list:
        sum += int(a_num)
    average = sum / len(a_list)
    return average

grades = [1, 25, 64, 74, 100, 82]
digits = "21313523235"
print(calculate_average(grades))
print(calculate_average(digits))