# conditional structure - program

'''
PROGRAM 03: CATEGORIES OF EMPLOYEES SALARY
    Calculate the incremental salary and total salary of employee taking in account:

    * Years of service     |   Salary increase rate
          1-5 years        |        10%
          6 years or +     |        15%
    
    * Another concepts     |    Salary increase rate
        boss               |        10%
        high education     |        5%
        phd                |        12%

    Definition of variables
        - y_service: years of service of employee (input)
        - concepts: description of concept (input)
        - incr_rate1: increase rate based on years of service
        - incr_rate2: increase rate based on another concepts
        - base_salary: basic salary of employee
        - incr_salary: incremental salary taking account incremental rates
        - total_salary: total value of salary
'''

def main():
    print("**** PROGRAM 03 ****")
    try:
        base_salary = float(input("Base salary (rubles):\t"))
        y_service = int(input("Enter years of service:\t"))
    except ValueError:
        print("Invalid input. Please enter numbers for salary and years.")
        return

    concepts = input("Enter concepts (boss/high education/phd):\t")

    # define rate by years of service
    if y_service >= 6:
        incr_rate1 = 0.15
    elif 1 <= y_service <= 5:
        incr_rate1 = 0.10
    else:
        incr_rate1 = 0.0

    # define rate by concept
    c = concepts.strip().lower()
    
    if c == "boss":
        incr_rate2 = 0.10
    elif c == "high education":
        incr_rate2 = 0.05
    elif c == "phd":
        incr_rate2 = 0.12
    else:
        incr_rate2 = 0.0

    # calculate the salaries
    incr_salary = base_salary * (incr_rate1 + incr_rate2)
    total_salary = base_salary + incr_salary

    print("*** Results ***")
    print(f"Incremental salary:\t{incr_salary:.2f} rubles")
    print(f"Total salary:\t\t{total_salary:.2f} rubles")


if __name__ == "__main__":
    main()
