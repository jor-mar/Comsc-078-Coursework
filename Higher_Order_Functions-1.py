"""
Written by Jordan Marcelo
Higher Order Functions Assignment:
1) square(x) returns x**2
2) fourth_power(x) returns x**4
3) summation(f, lower, upper) returns the sum of f evaluated from lower to upper, inclusive
Employs an anonymous lambda function that returns the square root of a number
"""
from math import sqrt


def square(x):
    """ This function calculates and returns the square of the input argument x """
    return x*x

def fourth_power(x):
    """ This function calculates and returns the fourth power of x.
    It uses neither x*x*x*x, x**4, nor math.pow(x, 4) """
    return square(x)*square(x)


def summation(f, lower_bound, upper_bound):
    """This function accepts arguments that include a function, lower bound,
    and upper bound. It then sums the values from the function for each of
    the numbers between the lower bound and upper bound, inclusive """
    # revise and update the code from the summation function that was
    # introduced in section 1.6 of the text

    total = 0
    for i in range(lower_bound, upper_bound+1):
        total += f(i)
    return total


def print_results(f, function_results, lower_bound, upper_bound, skip_lines=False):
    """This function accepts arguments that include a function, a string for the plural
    name of the function's output, lower bound, upper bound, and an optional boolean
    that skips two lines after printing if true. This function prints a string summarizing
    the results of the summation of the function by its bounds as calculated by the summation function."""

    answer = summation(f, lower_bound, upper_bound)
    print("The sum of " + str(function_results) + " of the numbers from " + str(lower_bound) + " to " + str(upper_bound) + " is " + str(answer))
    if skip_lines:
        print("\n")
    return print_results


def main():
    while True:
        print("User input:")
        lower_bound = int(input("Enter a lower bound for the sum: "))
        upper_bound = int(input("Enter an upper bound for the sum: "))

        print("\nProgram output:")
        print_results(square, "squares", lower_bound, upper_bound)(fourth_power, "the fourth powers", lower_bound, upper_bound)(lambda x: sqrt(x), "square roots", lower_bound, upper_bound, skip_lines=True)

if __name__ == "__main__":
    main()