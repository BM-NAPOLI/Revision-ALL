import random

number = random.randint(1, 20)
guess = int(input("Guess a number between 1 and 20: "))
if guess < number:
    print("Too low! Try again.")    
elif guess > number:
    print("Too high! Try again.")
else:
    print("Congratulations! You guessed the number.")