def binarySearch():
    objective = int(input('Select a number:  '))
    epsilon = 0.00000000000001#Set precision
    down = 0.0
    highest = max(1.0, objective)#Only return the value higher inte the function
    answer = (highest + down) / 2
    while abs(answer**2 - objective) >= epsilon:
        #print(f'down = {down}, highest = {highest}, answer = {answer}')
        if answer**2 < objective:
            down = answer
        else:
            highest = answer
        answer = (highest + down) / 2
    print(f'Squere root of {objective} is {answer}')

def aproximation():
    objective = int(input('Catch a number:  '))
    epsilon = 0.01
    pss = epsilon**2
    answer = 0.0
    #'abs' return the absolute value
    while abs(answer**2 - objective) >= epsilon and answer<= objective:
        print(abs(answer**2 - objective), answer)
        answer += pss
    if abs(answer**2 - objective) >= epsilon:
        print(f'Not found the square root of {objective}')
    else:
        print(f'The square root of {objective} is {answer}')

def enumeration():
    objective = int(input('Select a integer: '))
    answer = 0
    while answer**2 < objective:
        answer +=1
    if answer**2 == objective:
        print(f'Square branch of {objective} is {answer}')
    else:
        print(f'{objective} hasn´t a square branch')


while True:
    print('Forms to get a square root in python!')
    print('1) Binary search')
    print('2) Aproximation')
    print('3) Enumeration')
    print('4) Exit')

    x = int(input('Select an option:   '))

    if x == 1:
        print('Binary search method')
        binarySearch()
        
    elif x == 2:
        print('Aproximation method')
        aproximation()
        
    elif x == 3:
        print('Enumeration method')
        enumeration()
    elif x == 4:
        print('Bye bye!')
        break