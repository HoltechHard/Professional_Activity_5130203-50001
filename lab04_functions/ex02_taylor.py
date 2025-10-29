'''
    WEEK 02 - PROGRAM 04: TAYLOR SERIES
    Write a program to calculate the cosine function using Taylor's formula. 
    The argument x is entered by the user from the keyboard, and the series boundary n 
    is defined as a constant with a value equal to 10.
    Calculate the approximate value of cos(x).

    Definition of variables: 
        - x: argument of cosin function
        - last_term: value of the current term of taylor serie
        - result: final sum of all terms of taylor serie
'''

# Taylor Series Approximation for cos(x)

def taylor_cos(x, n=10):
    last_term = 1.0
    result = last_term

    print("Series terms:")
    for i in range(1, n + 1):
        last_term *= -1 * (x ** 2) / ((2 * i - 1) * (2 * i))
        print(f"{last_term:.10f}", end="  ")
        result += last_term

    print("\n")
    return result


def main():
    # Read input from user
    x = float(input("Enter a value for x: "))

    # Calculate using Taylor series
    result = taylor_cos(x)

    print(f"\nFinal result:")
    print(f"cos({x}) = {result:.10f}")


if __name__ == "__main__":
    main()
