stopping_value = 1000
user_list = []
user_input = int(input("Enter a first number here: "))
while user_input != stopping_value:
    while user_input > 100 or user_input < 1:
        user_input = int(input("Value is outside of the range. Try again: "))
        if user_input == stopping_value:
            break
    if user_input == stopping_value:
        break
    user_list.append(user_input)
    user_input = int(input("Enter third number: "))
print('Output: ')

for x in user_list:
    print(x)
