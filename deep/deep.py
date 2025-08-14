deep_thoughts = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')

#making sure spaces before and after the input are removed and all characters are lowercase
deep_thoughts = deep_thoughts.strip().lower()

if deep_thoughts == '42' or deep_thoughts == 'forty two' or deep_thoughts == 'forty-two':
    print('yes')
else:
    print('no')
