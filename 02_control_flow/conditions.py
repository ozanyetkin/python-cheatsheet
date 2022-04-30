a = 5
b = 3
c = 8

if a > b:
    print(a + b)
elif c > a:
    print(a + c)
else:
    print(a + b + c)

if a > b:
    print(a + b)
if c > a:
    print(a + c)
else:
    print(a + b + c)

if a > b:
    print(a + b)
if c > a:
    print(a + c)

print(a + b + c)

# if Statement
 
test_value = 100
 
if test_value > 1:
  # Expression evaluates to True
  print("This code is executed!")
 
if test_value > 1000:
  # Expression evaluates to False
  print("This code is NOT executed!")
 
print("Program continues at this point.")

# else Statement
 
test_value = 50
 
if test_value < 1:
  print("Value is < 1")
else:
  print("Value is >= 1")
 
test_string = "VALID"
 
if test_string == "NOT_VALID":
  print("String equals NOT_VALID")
else:
  print("String equals something else!")

pet_type = "fish"
 
if pet_type == "dog":
  print("You have a dog.")
elif pet_type == "cat":
  print("You have a cat.")
elif pet_type == "fish":
  # this is performed
  print("You have a fish")
else:
  print("Not sure!")
