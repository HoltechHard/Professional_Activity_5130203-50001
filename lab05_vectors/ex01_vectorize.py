# LIST 04 - TASK 01: BASIC OPERATIONS WITH VECTORS
# Using functions and procedures, enter vectors A and B with dynamic memory
# and let the user define the number of elements. Make the next operations:
#
# [1]. Create a procedure that allows the user to enter vector elements from the keyboard.
# [2]. Create a procedure that allows the user to print vector elements.
# [3]. Calculate the Euclidean distance between two vectors.
# [4]. Calculate the dot product of two vectors A and B using the linear combination formula.
# [5]. Calculate the angle formed between vectors A and B.
# [6]. Create a vector C that concatenates vectors A and B with elements sorted in ascending order.
#      Use the bubble-sort algorithm.
# [7]. Using the ordered vector C, calculate the statistical measures:
#      - math expectation
#      - standard deviation
#      - median
#
# Definition of variables:
#     - n: number of elements of vector
#     - a, b: vectors
#     - c: vector result of unify a, b
#     - e_dist: output result of calculate euclidean distance
#     - s_prod: output result of calculate scalar product
#     - angle: output result of calculate angle between 2 vectors using functions with call by value
#     - angle2: output result of calculate angle between 2 vectors using procedure
#     - mean: output result of calculate mean of ordered vector C
#     - std: output result of calculate standard deviation of ordered vector C
#     - median: output result of calculate median of ordered vector C

import math

# header of functions defined by user
def input_num_elements():
    n = 0
    while n <= 0:
        n = int(input("\nNumber of elements: "))
    return n

def allocate_memory(n):
    return [0] * n

def input_vector(n, x):
    for i in range(n):
        x[i] = int(input(f"X[{i}]: "))

def print_vector(n, x):
    for i in range(n):
        print(x[i], end="  ")
    print()

def euclidean_dist(n, x, y):
    dist = 0
    for i in range(n):
        dist += (x[i] - y[i]) ** 2
    return math.sqrt(dist)

def scalar_product(n, x, y):
    sp = 0
    for i in range(n):
        sp += x[i] * y[i]
    return sp

def calculate_module(n, x):
    mod = 0
    for i in range(n):
        mod += x[i] ** 2
    return math.sqrt(mod)

def calculate_angle(n, x, y):
    sp = scalar_product(n, x, y)
    mod_x = calculate_module(n, x)
    mod_y = calculate_module(n, y)
    return math.acos(sp / (mod_x * mod_y))

def unify_vector(n, x1, x2, y):
    for i in range(n):
        y[i] = x1[i]
        y[i + n] = x2[i]

def bubble_sort(n, x):
    for i in range(n - 1):        
        for j in range(0, n - i - 1):
            if x[j] > x[j + 1]:                
                x[j], x[j + 1] = x[j + 1], x[j]

def calculate_mean(n, x):
    sum_val = 0.0
    for i in range(n):
        sum_val += x[i]
    return sum_val / n

def calculate_std(n, x):
    mean = calculate_mean(n, x)
    std = 0.0
    for i in range(n):
        std += (x[i] - mean) ** 2
    return math.sqrt(std / n)

def calculate_median(n, x):
    if n % 2 != 0:
        return x[(n - 1) // 2]
    else:
        return (x[n // 2 - 1] + x[n // 2]) / 2.0

# main function
def main():
    # define variables
    n = input_num_elements()
    a = allocate_memory(n)
    b = allocate_memory(n)
    # input vectors A and B
    print("\nInput the elements for vectors: ")
    print("\nA: ")
    input_vector(n, a)
    print("\nB: ")
    input_vector(n, b)

    # print elements of vectors A and B
    print("\nVector A: ")
    print_vector(n, a)
    print("\nVector B: ")
    print_vector(n, b)

    # calculate euclidean distance
    e_dist = euclidean_dist(n, a, b)
    print(f"\nEuclidean distance = {e_dist}")

    # calculate scalar product
    s_prod = scalar_product(n, a, b)
    print(f"\nScalar product = {s_prod}")

    # calculate angle using function by call
    angle = calculate_angle(n, a, b)
    print(f"\nCalculate angle using function = {angle}")

    # unify vectors a, b in vector c
    c = allocate_memory(2 * n)
    unify_vector(n, a, b, c)
    print("\nUnified vector: ")
    print_vector(2 * n, c)

    # apply sort in ascendent order
    bubble_sort(2 * n, c)
    print("\nSorted vector: ")
    print_vector(2 * n, c)

    # print statistical results
    mean = calculate_mean(2 * n, c)
    print(f"\nMean = {mean}")
    std = calculate_std(2 * n, c)
    print(f"\nStd = {std}")
    median = calculate_median(2 * n, c)
    print(f"\nMedian = {median}")

if __name__ == "__main__":
    main()