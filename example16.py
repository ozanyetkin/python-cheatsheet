# a_number = int(input("Bir sayi giriniz: "))
"""
summation = 0
for i in range(1, a_number // 2 + 1):
    if a_number % i == 0:
        summation += i
"""
perfect_numbers = []

for a_number in range(2, 10000):
    summation = 0
    divisor = 1
    while divisor <= a_number // 2:
        if a_number % divisor == 0:
            summation += divisor
        divisor += 1

    if summation == a_number:
        # print(f"{a_number} bir mukemmel sayidir")
        perfect_numbers.append(a_number)
    else:
        # print(f"{a_number} bir mukemmel sayi degildir")
        pass

print(perfect_numbers)
