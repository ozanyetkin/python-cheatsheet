primes = [2, 2, 3, 5, 7, 11, 13, 17]
primes.append(21)
primes.insert(2, 4)

# print(primes.pop(2))
# print(primes.count(26))
# print(primes)

"""
for p in primes:
    if p >= 7:
        print(f"sayi = {p}, ve bu sayi 7'ye buyuk esit")
    else:
        print(f"sayi = {p}, ve bu sayi 7'den kucuk")
"""
empty_list = []

a_list = [2, "two", [2.4, 5.6, [7.4]], ["hello world"]]
# print(a_list[2][0])

contact_list = [["Ahmet", "Cinar", "ahmet@msn.com", "+905367453209"], ["Mahmut", "Tuncer", "lo@halay.com", "583-234-64-98"]]
"""
for contact in contact_list:
    print(f"Isim : {contact[0]}")
    print(f"Soyisim : {contact[1]}")
    print(f"Mail : {contact[2]}")
    print(f"No : {contact[-1]}")
"""
a_list = [4, 13, 22, 19, 4, 5, 16, 18]
sorted_list = a_list.copy()
sorted_list.sort(reverse=True)
print(sorted_list)