'''
    WEEK 02 - PROGRAM 02: PRIME NUMBERS 
    Develop a program that allows you to print prime numbers in the range [2, 100] on the terminal. 
    Definition of variables: 
        - n: analized number in the range [2, 100] 
        - div: potential divisor of n
'''

def main():
    print("**** PROGRAM 02 ****")

    # definition of variables
    print("Prime numbers:")

    # cycle to check each number in range [2, 100]
    for n in range(2, 101):
        div = 2
        # cycle to verify potential divisors [2, n-1]
        while div < n:
            if n % div == 0:
                break  # stop if a divisor is found
            div += 1

        # print prime number when unique divisor found was the same number
        if div == n:
            print(n, end="  ")


if __name__ == "__main__":
    main()
