"""
a_number = input("bir sayi giriniz: ")

if a_number.isnumeric():
    a_number = int(a_number)
else:
    print("hatali giris yaptiniz")
    # exit()

try:
    a_number = int(a_number)
except :
    a_number = input("hatali giris yaptiniz, lutfen bir sayi giriniz: ")

a_number = int(a_number)
"""
nums = [65, 27, "-", 48, 95, "-", 78, 96, 100]

total = 0
len = len(nums)
for num in nums:
    try:
        total += num
    except TypeError:
        len -= 1

avg = total / len
print(avg)

test_cases = [
    "username@companyname.com", 
    "", "usernamecompanyname.com", 
    "username@companynamecom", 
    "user name@companyname.com"
]

"""
for test in test_cases:
    index = test.find("@")
    if index != -1:
        user_name = test[0:index]
    else:
        user_name = ""
    print(user_name)
"""

test = "usernamecompanyname.com"
for i, t in enumerate(test):
    if t == "@":
        index = i
try:
    user_name = test[0:index]
except NameError:
    user_name = ""

print(user_name)
