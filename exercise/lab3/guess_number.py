import random

def main():
    number = random.randint(1,5)

    name = input("Hello! What is your name?")
    print(f"Cool! Great to meet you, {name}. Let's play!\
        I'm thinking of a number between 1 and 5.")
    
    guess = int(input("Enter your guess"))

    if guess > number:
        print(f"Unfortunately, your guess was too high.\
        my number was:{number}")

    if guess < number:
        print(f"Sorry... your guess was too low.\
        My number was:{number}")

    if guess == number:
        print("Yay! Your guessed my number!")

    
main()


