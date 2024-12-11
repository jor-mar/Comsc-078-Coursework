def power(base, exponent):
    """Returns base^exponent"""
    if exponent == 0: # disqualifies base case since b^0 = 1
        return 1
    return base * power(base, exponent-1) # returns base times itself for exponent number of times

def main():
    base = int(input('Enter a base: ')) # takes base input
    exponent = abs(int(input('Enter a power: '))) # takes exponent input with non-negative integer assumption
    print(power(base, exponent)) # prints result

if __name__ == '__main__':
    main()