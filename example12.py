user_input = input("bir sayi giriniz ")

while not user_input.isnumeric():
    user_input = input("bir sayi giriniz ")

int(user_input)
