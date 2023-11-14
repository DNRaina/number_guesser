import random

def guess_number(limit,number):
    random_number = random.randint(1,number)
    
    while limit > 0:
        print("What is your guess ?")
        guess = int(input())

        if guess == random_number:
            print("you got it right")
            break
        elif guess > number :
            print("guessed number out of range")
            print(f"you have {limit} guesses left")
            limit -= 1
        else:
            limit -= 1
            print("the guess is incorrect")
            print(f"you have {limit} guesses left")
    
    print("Game over")
    print(f"the correct number was {random_number}")
    