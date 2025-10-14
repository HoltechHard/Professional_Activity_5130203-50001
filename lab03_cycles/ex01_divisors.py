'''
    WEEK 02 - PROGRAM 01: DIVISORS OF NUMBER 
    
    Develop a program that, when a number in the range [2, 1000] is entered, 
    displays all the divisors of the number, the number of divisors, and the sum of the specified divisors. 
    Definition of variables: 
        - n: input number [2, 1000] 
        - i: analized number as potential divisor [1, n] 
        - num_divisors: number of divisors 
        - sum_divisors: sum of all divisors
'''

def main():
    print("**** PROGRAM 01 ****")
    
    # definition of variables
    n = 0
    num_divisors = 0
    sum_divisors = 0

    # input the number by user
    while True:
        n = int(input("Enter the n: "))
        if 2 <= n <= 1000:
            break

    # cycle to verify potential divisors of n
    print("Divisors:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
            num_divisors += 1
            sum_divisors += i

    print(f"\nNumber of divisors: {num_divisors}")
    print(f"Sum of divisors: {sum_divisors}")


if __name__ == "__main__":
    main()
