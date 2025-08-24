#ask for input
words = input('Enter a text? ')

#empty string
new_words = ''

#loop through each character in given input
for char in words:

    #lowercase check if character is vowel 
    if char.lower() in 'aeiou' :
        continue
    
    #build your word
    else:
        new_words += char

print(new_words)