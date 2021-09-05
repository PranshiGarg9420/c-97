import random
print("Number guessing game")
number= random.randint(1,9)
chances=0
print("Guess the number between 0-9")

while chances<5:

    guess=int(input("Enter your guess:"))


    if guess==number:
        print("Congratulations! you guessed the number right")
        break

    elif guess<number:
        print("You guessed too low!")

    else:
        print("You guessed too high!")

    chances+=1


if not chances<5:
    print("YOU LOST!!,The number is",number)
