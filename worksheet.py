x = 5
y = x

x += 1
print(id(x))
print(id(y))
# Call by reference
def fun_list(x):
    print(x, id(x)) 
    x.append(1)
    print(x, id(x)) 

my_list = [5]
print(my_list, id(my_list))

fun_list(my_list)
