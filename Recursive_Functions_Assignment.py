"""Jordan Marcelo recursive functions assignment for COMSC 078 @ EVC 9/16/24
This program tests if the display_em and add_em functions work with user-inputted lower and upper bounds"""

def display_em(lower, upper):
    """ This recursive function displays the consecutive integers
    from its lower to its upper bounds """
    if lower == upper:
        print(str(upper))
    else:
        print(str(lower))
        display_em(lower+1, upper)

def add_em(lower, upper):
    """ This recursive function calculates the sum of the consecutive
    integers from its lower to its upper bounds"""
    if lower == upper:
        return upper
    else:
        return lower + add_em(lower+1, upper)

def applyToEach(f, lower_bound, upper_bound):
    """ This higher-order function applies the included function
    to its lower and upper bound arguments"""
    return f(lower_bound, upper_bound)

def main():
    """This prompts a user for lower and upper bound numbers
    and applies those numbers to the add_em and display_em functions
    while using the higher-order applyToEach function and displaying
    the results."""
    x = int(input("Enter a lower bound: "))
    y = int(input("Enter an upper bound: "))

    print("\nThe consecutive integers:")
    applyToEach(display_em, x, y)

    print("\nAdd up to " + str(applyToEach(add_em, x, y)))

if __name__ == "__main__":
    main()