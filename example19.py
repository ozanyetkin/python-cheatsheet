# Tek bir sayi alacak, o sayiya kadar olanlarin kendiyle aralarinda asallik durumunu test edecek
# 12 verdiysek eger: 1, 5, 7, 11
from math import floor, sqrt
my_num = 12

def co_prime(num_1, num_2):
    '''Iki sayi verildiginde aralarinda asal olup olmadiklarini test eder'''
    if num_1 % 2 == 0 and num_2 % 2 == 0:
        return False
    else:
        for i in range(3, floor(min(sqrt(num_1), sqrt(num_2))) + 1, 2):
            if num_1 % i == 0 and num_2 % i == 0:
                return False
        return True

def prime_among(a_number: int):
    '''Bir sayi verildiginde o sayiya kadar arasinda asal tum sayilari bulur'''
    co_primes = [1]
    for i in range(2, a_number):
        if co_prime(a_number, i) == True:
            co_primes.append(i)
    return co_primes

print(prime_among(12))
prime_among()