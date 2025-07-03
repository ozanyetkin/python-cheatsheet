# // Floor division Arithmetic Operator which gives quotient
# % Modulus Arithmetic Operator

number1 = input('Enter a number in the range 1 to 86400:')
num_of_secs = int(number1)

num_of_mins = num_of_secs//60
num_of_secs = num_of_secs % 60

num_of_hours = num_of_mins//60
num_of_mins = num_of_mins % 60

num_of_days = num_of_hours//24
num_of_hours = num_of_hours % 24

print(num_of_hours, "hours", num_of_mins, "mins", num_of_secs, "secs")

# Revisit after Formatting
print("%d hours, %d minutes, %d seconds " % (num_of_hours, num_of_mins, num_of_secs))
print("%d days, %d hours, %d minutes, %d seconds " % (num_of_days, num_of_hours, num_of_mins, num_of_secs))
print("%d days, %d hours, %d minutes, %d seconds " % (num_of_days, num_of_hours, num_of_mins, num_of_secs))