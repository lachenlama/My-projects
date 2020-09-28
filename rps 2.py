# Rock Paper and Scissor


def main(n1,n2):
    if n2 == 1:
        n2 = ("rock")

    elif n2 == 2:
        n2 = ('paper')


    elif n2 == 3:
        n2 = ('scissor')

    else:
        pass

    print(f'{n1} vs {n2}')
    if (n1 == 'rock' and n2 == 'scissor') or (n1 == 'paper' and n2 == 'rock') or (n1 == 'scissor' and n2 == 'paper'):
        print('You win.')

    elif (n2 == 'rock' and n1 == 'scissor') or (n2 == 'paper' and n1 == 'rock') or (n2 == 'scissor' and n1 == 'paper'):
        print('You loose.')

    elif (n1 == n2):
        print('Tie')

print('Select the number\n\n1 for rock\n2 for paper\n3 for scissor')
while True:
    n1 = int(input('Enter your choice: '))

    if n1 == 1:
        n1 = ("rock")
        break
    elif n1 == 2:
        n1 = ('paper')
        break

    elif n1 == 3:
        n1 = ('scissor')
        break
    else:
        pass

from random import randint
n2 = randint(1,3)

main(n1,n2)