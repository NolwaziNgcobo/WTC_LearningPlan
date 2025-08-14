#implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer

def main():
    mass = int(input('Enter mass in kilograms? '))
    final_energy = energy(mass)
    print('Energy in joules:', final_energy)


def energy(number):
    speed = 300000000
    return number * speed**2 #formula


main()
