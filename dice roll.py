'''Roll a dice'''

from random import randint

def main():
    print('Dice has been rolled.')
    roll = int(randint(1,6))
    print('\nEnter your choice i.e number between 1 to 6.')
    c = int(input('Enter choice: '))

    if c == roll:
        print('Congratulation! your guess is correct.')

    else:
        print('better luck next time.')


def dice_roll():
    while True:
        print('Enter y to roll the dice or n to stop.')
        choice_roll = str(input(": "))
        if choice_roll == 'y':
            main()
        elif choice_roll == 'n':
            break

dice_roll()
print('Thank you.')