name_user_one = input('Write your name: ')
num_1 = int(input('Write your age: '))
name_user_two = input('Write your name: ')
num_2 = int(input('Write your age: '))

if num_1 > num_2:
    print(f'The first user {name_user_one} is older that the second one')
elif num_1 < num_2:
    print(f'The first user {name_user_two} is older that the first one')
else:
    print(f'Both users {name_user_one}, {name_user_two} have the same age')