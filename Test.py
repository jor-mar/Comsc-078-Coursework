def pass_it(x, y):
    z = x * y

    result = get_result(z)

    return (result)


def get_result(number):
    z = number + 2

    return (z)


num1 = 3

num2 = 4

answer = pass_it(num1, num2)

print(answer)







def multiply(x, y):
    if y == 1:
        return x
    else:
        return x + x*(y-1)


# from BasicMath import multiply

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base*power(base, exponent-1)

def Test(f, x, y):
    """This higher-order function accepts a function and two variables"""
    return f(x, y)

def main():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print()

    print("The product of " + str(x) + " times " + str(y) + " is " + str(Test(multiply, x, y)))
    print("But " + str(x) + " raised to the power of " + str(y) + " is " + str(Test(power, x, y)))
    print()

if __name__ == "__main__":
    main()