'''To solve a quadratic equation'''

def values():
    print('y to enter values or n to end the process.')
    while True:
        process_choice = str(input("y or n: "))
        if process_choice == "y":
            logged()
        else:
            print('Thank you.')
            break

def logged():
    print("In the equation i.e ax^2+bx+c")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    import cmath
    d = ((b**2)-4*a*c)
    num1 = ((-b+cmath.sqrt(d))/(2*a))
    num2 = ((-b+cmath.sqrt(d))/(2*a))
    print(f"x is equal to {num1} and {num2}.")

values()