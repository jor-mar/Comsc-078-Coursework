import random # imports random module to handle RNG

random.seed(1000) # sets seed to 1000

random_numbers = [] # defines an empty list to add all the random numbers to
for i in range(50): # runs the following code 50 times
    random_numbers.append(random.randint(0, 100)) # adds a new random number from 0-100 to the list
print(random_numbers) # displays the list