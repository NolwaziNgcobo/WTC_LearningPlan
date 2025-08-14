#prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
course_name = input('What is the name of this course? ')

#substring my input
name = course_name.split()

#use '...' to join the string
final_name = '...'.join(name)
print(final_name)
