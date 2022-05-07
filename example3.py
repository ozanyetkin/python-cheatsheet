# Write a Python program that prompts for a number.
# Take that number, add 2, multiply by 3, subtract 6, and divide by 3.

input1 = input('Enter a number:')
number = ((int(input1) + 2) * 3 - 6) / 3

print('type(input1)', type(input1), 'type(number)', type(number))

print('Input:', input1, 'Number', number)
print(input1, number)
print('%s %f' % (input1, number))
