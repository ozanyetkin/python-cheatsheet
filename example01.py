num_1 = 10.2

if type(num_1) == int:
    if num_1 % 2:
        print("This is an odd number")
    else:
        print("This is an even number")
else:
    print("This is not an integer")
    num_1 = int(num_1)
    print("When converted to integer: " + str(num_1))
    if num_1 % 2:
        print(str(num_1) + " is odd")
    else:
        print(str(num_1) + " is even")
