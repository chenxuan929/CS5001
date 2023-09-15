'''
    Cs5001
    Lab 3
    Assignment Part 1b
'''

import random

max_guesses = 5

def main():
    number = random.randint(1, 100)
    name = input("Hello! What is your name?")
    print(f"Cool! Great to meet you, {name}.Let's play!")
    print(" I'm thinking of a number between 1 and 100.You have 5 guesses.")
    
    

    num_guess = 0
    found = False
    
    while num_guess < max_guesses and not found:
        num_guess = num_guess + 1
        user_guess = int(input("Emter your guess"))
        
        if user_guess == number:
            print("Yay! You guessed my number!")
            found = True
        elif user_guess < number:
            print("Nope. Too low.")
        elif user_guess > number:
            print("Nah. Too high")
       
    if found:
        print(f"Great job! You won in {num_guess} tries")
    else:
        print(f"Nice try, but you lost this time. My number was :{number}")

if __name__ == "__main__":
    main()
