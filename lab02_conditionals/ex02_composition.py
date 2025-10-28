'''
    PROGRAM 02: COMPOSITION OF FUNCTIONS
'''

import math

def main():
    print("**** PROGRAM 02 ****")

    # define variables
    try:
        a = float(input("Enter a:\t"))
        b = float(input("Enter b:\t"))
        x = float(input("Enter x:\t"))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # calculate function F(a, b)
    if a < b:
        F = math.sqrt(a) * b
    elif b < 0:
        F = a**2 + b
    else:
        F = a - b

    # calculate function G(x)
    if x <= 1:
        G = 0
    elif x <= 2:
        G = 2 * x - 2
    elif x <= 3:
        G = 2
    elif x <= 4:
        G = -2 * x + 8
    else:
        G = 0

    # calculate results
    print("Results:")
    print(f"F + G = {(F + G):.2e}")
    print(f"F * G = {(F * G):.2e}")
    
    if G != 0:
        print(f"F / G = {(F / G):.2e}")
    else:
        print("F / G = Undefined (division by zero)")

if __name__ == "__main__":
    main()
