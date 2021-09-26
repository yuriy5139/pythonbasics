# Task1: working with variables

def task1():
    try:
        user_input = input("Please enter integer variable ")
        a = int(user_input)
    except ValueError:
        print("You entered a non-integer value")
    else:
        print("Well done, the type of your variable is", type(a))

    allowed_bool = ['True', 'False']
    user_input = input("Please enter a Boolean variable ")
    if user_input in allowed_bool:
        print("Well done, the type of your variable is", type(bool(user_input)))
    else:
        print("Only True and False values are allowed")


# Task2: Time extractor
def task2():
    timerange = int(input("Enter time in seconds "))
    hours = timerange // 3600
    minutes = (timerange - hours * 3600) // 60
    seconds = timerange % 60
    print("The time period contains {} hours, {} minutes and {} seconds".format(hours, minutes, seconds))


# Task3: Number summation
def task3():
    n = input("Enter a single number between 0 and 9 ")
    ni = int(n)
    print("The sum of {} + {} + {} is {}".format(n, n + n, n + n + n, ni + (ni * 10 + ni) + (ni * 100 + ni * 10 + ni)))


# Task4: biggest digit in a number with while and arithmetic operations
def task4():
    try:
        num = input("Please enter a positive number ")
        if int(num) <= 0:
            raise ValueError
    except ValueError:
        print("you have to enter only positive integer numbers")
    else:
        i = 0
        max_digit = int(num[0])
        while i < len(num):
            if int(num[i]) > max_digit:
                max_digit = int(num[i])
            i += 1
        print("The biggest digit in {} is {}".format(num, max_digit))


# Task5: company success measure

def task5():
    try:
        revenue = int(input("Please enter revenue "))
        spending = int(input("Please enter spendings "))
        employees = int(input("Please enter employees "))
        if revenue <= 0 or spending <= 0 or employees <= 0:
            raise ValueError
    except ValueError:
        print("Revenue, spending and employee number shall all be positive numbers")
    else:
        if revenue >= spending:
            profitability = revenue / spending
            per_empl = (revenue - spending) / employees
            print("The company is profitable with profitability {:.3f}".format(profitability))
            print("Per-employee profit is {:.3f}".format(per_empl))
        else:
            print("The company is not profitable")

#Task6: Sports tracking
def task6():
    try:
        start_dist = int(input("Please enter first day distance "))
        target = int(input("Please enter target distance "))
        if target <= start_dist:
            raise ValueError
    except ValueError:
        print("All distances shall be int numbers with target > first day distance")
    else:
        days = 0
        curr_dist = start_dist
        while curr_dist < target:
            curr_dist = curr_dist * 1.1
            days += 1
        print("The required number of days for training is {}".format(days))

if __name__ == '__main__':
    # Write the function you want to test here
    #task1()
    #task2()
    #task3()
    #task4()
    #task5()
    task6()