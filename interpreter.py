#prompt the user for arithmetic expression and split the expression into parts
print('Enter an arithmetic expression. e.g 1 + 1')
expression = input('Expression: ').split()

#if user input is 3 substrings convert x and z to float
if len(expression) == 3:
    x = float(expression[0])
    y = expression[1]
    z = float(expression[2])

    #calculation/interpretation condition
    if y == '+':
        result = x + z
    
    elif y == '-':
        result = x - z

    elif y == '*':
        result = x * z

    elif y == '/':
        result = x / z

    else:
        result = 0.0

    #round result to 1 decimal place and desplay
    print(round(result, 1))

else:
    print('0.0')




