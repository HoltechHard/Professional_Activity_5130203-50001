# conditional structure - program

'''
PROGRAM 01: KINETIC ENERGY OF ELECTRON
    Definition of variables
        - me: electron mass (input)
        - c: speed of light (input)
        - v: speed of electron (input)
        - Ek: kinetic energy of electron (output)
        - E: non-relative energy of electron (output)
'''

import math

def main():
    print("**** PROGRAM 01 ****")

    # constants (SI units)
    me = 9.1e-31      # electron mass (kg)
    c = 2.998e8       # speed of light (m/s)

    # input
    try:
        v = float(input("Enter the speed of electron (m/s):\t"))
    except ValueError:
        print("Invalid input! Enter a numeric value for speed.")
        return

    # Relativistic kinetic energy Ek
    if v >= c:
        Ek = None
    else:
        gamma = 1.0 / math.sqrt(1.0 - (v / c) ** 2)
        Ek = me * (c ** 2) * (gamma - 1.0)

    # Classical (non-relativistic) kinetic energy E
    E = 0.5 * me * (v ** 2)

    # output
    if Ek is None:
        print("It's not possible to calculate the kinetic energy of the electron (v >= c).")
    else:
        print(f"Kinetic energy of electron: {Ek:.6e} J")

    print(f"Non-relative energy of electron: {E:.6e} J")


if __name__ == "__main__":
    main()
