#ask for user input
print('Enter variable in camelCase')
camelCase = input('camelCase: ')

#start your string empty
snake_case = ''

#building your new string by looping through the given string, adding lowercases and adding underscore and the lowercase version to you new string
for char in camelCase:
    if char.isupper():
        snake_case += '_' + char.lower()
    else:
        snake_case += char

print(snake_case)