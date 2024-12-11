def main():
    square = 0 # the initial square (square of 0) is 0
    for i in range(11): # loops 10 times, from 0 to 10 but not 11
        if i > 0: # removes base case where 0^2 = 0
            square += 2*(i-1)+1 # adds to known value to find next value
        print(f'{i}^2 = {square}') # displays result

if __name__ == '__main__':
    main()