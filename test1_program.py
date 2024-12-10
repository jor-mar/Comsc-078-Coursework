"""Jordan Marcelo COMSC 78 @EVC Test #1 Program"""
import random

def is_even(n):
    """Receives an integer and returns a boolean describing whether the received is an even number."""
    return n % 2 == 0 # returns boolean representing whether the number being even (perfectly divisible by 2)

def random_array(size, start, stop):
    """Creates an array of random numbers of length size, with each element being an int between start and stop, inclusive."""
    array = [] #creates an empty array that will be appended
    for i in range(size): #starts appending the empty array to the specified size with random ints
        x = random.randint(start, stop) #creates a new random integer every loop where it is in range [start, stop]
        array.append(x) #appends the array with the new random int each time
    return array #returns the array full of random ints

def count_qualified(array, f):
    """Counts the number of elements in an array that return true when passed individually through function f."""
    count = 0 #starts counting the number of elements in the function that return true when passed through f
    for i in array: #loops through the elements of array
        if f(i): #if f(1) returns true, the following executes:
            count += 1 #the counter of elements that return true when passed through f is increased
    return count #finally, the count is returned

def main():
    """Returns number of even numbers in length 100 arrays of random numbers as long as user input allows."""
    while True: #executes self continuously until broken
        num_evens = count_qualified(random_array(100, 1, 1000), is_even) #counts the number of evens in an array of length 100 whose random numbers are in range [1, 1000]
        print("Out of a hundred random numbers,", 100-num_evens, "were odd, and", num_evens, "were even.") #tells the user the number of ints in the array with length 100 that are even and odd
        answer = str(input("Would you like to run the program again (Y/N): ")).lower() #asks user if they would like to continue and converts their answer to lowercase
        if answer != "y": #checks if the user's answer (converted to lowercase) is valid to continue programming
            break #if the user's input is invalid (anything other than Y or y), the program stops

if __name__ == "__main__": #boilerplate code that checks to make sure this code is meant to be running
    main() #runs main if this code is meant to be running