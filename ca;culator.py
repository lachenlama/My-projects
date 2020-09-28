#Calculator

def add(n1,n2):
    sum = n1 + n2
    return sum
def  sub(n1,n2):
    sub = n1 - n2
    return sub
def multiply(n1,n2):
    product = n1 * n2
    return product
def division(n1,n2):
    div = n1 / n2
    return div

while True:
    print('Enter the values for calculation below; ')
    v1 = float(input(':'))
    v2 = float(input(':'))
    print('Enter\n1 for addition,\n2 for substitution,\n3 for multiply,\n4 for division.')
    c = int(input('Enter: '))

    if c == 1:
        a = add(v1,v2)
        print(f'The sum of {v1} and {v2} is {a}')
    elif c == 2:
        s = sub(v1,v2)
        print(f'The subtraction of {v1} and {v2} is {s}')
    elif c == 3:
        m = multiply(v1,v2)
        print(f'The product of {v1} and {v2} is {m}')
    elif c == 4:
        d = division(v1,v2)
        print(f'The quotient of {v1} and {v2} is {d}')
    else:
        print('Invalid choice try again.')


