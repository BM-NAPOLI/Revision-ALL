import random

number = random.randint(1, 100)
guess = None    
while guess != number:
    guess = int(input("Enter a number betwieen 1 and 100: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")    

