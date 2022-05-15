user_number = input("bir sayi giriniz ")

while user_number.isnumeric() == False or len(user_number) != 6:
    user_number = input("bir sayi giriniz ")
"""
sum = 0
for i in range(len(user_number)):
    sum += int(user_number[i])
average = sum / len(user_number)
print(average)
"""
sum = 0
for digit in user_number:
    sum += int(digit)
average = str(int(sum / len(user_number)))

print(average)
# print("hello".replace("h", ""))
# print("hello".find("u"))
# 124468 ilk ortalama = 4, sayi 1268 yeni ortalama = 4

# while user_number.find(str(average)) > -1:
while average in user_number:
    user_number = user_number.replace(average, "")
    sum = 0
    for digit in user_number:
        sum += int(digit)
    average = str(int(sum / len(user_number)))

print(user_number)
