def dec2hex(n):
    """Converts a decimal to hex recursively"""
    if n == 0: # disqualifies base case since remainder of 0 is not represented
        return ''
    key = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F') # is the key for remainder classification
    return dec2hex(n//16) + key[n%16] # recursively builds hex representation of a decimal number, last computed number is first in returned string

def main():
    decimal = int(input('Enter a decimal number: ')) # only considers whole numbers
    if decimal == 0: # removes base case where there is no meaningful point in using above function
        print('The hexadecimal equivalent is: 0')
    else:
        hex_value = dec2hex(decimal) # computes hex representation & assigns to a variable
        print(f'The hexadecimal equivalent is: {hex_value}') # displays result

if __name__ == '__main__':
    main()