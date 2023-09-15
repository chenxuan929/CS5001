import random

# sets different number to represent different polemon in order
def get_player(num):
    if num == 1:
        return 'Bulbasaur'
    elif num == 2:
        return 'Charmander'
    elif num == 3:
        return 'Butterfree'
    elif num == 4:
        return 'Rattata'
    elif num == 5:
        return 'Weedle'
    elif num == 6:
        return 'Pikachu'
    elif num == 7:
        return 'Sandslash'
    elif num == 8:
        return 'Jigglypuff'
    elif num == 9:
        return 'Raichu'
    else:
        num == 10
        num == 101
        return 'Diglett'
# get player's choice in RPS game
def player_choice(player):
    if player == 1:
        player_choice_name = 'ROCK'
        return 'ROCK'
    elif player == 2:
        player_choice_name = 'PAPER'
        return 'PAPER'
    else:
        player_choice_name = 'SCISSORS'
        return 'SCISSORS'
    
# get the computer choice in RPS game
def computer_choice(computer):
    if computer == 1:
        computer_choice_name = 'ROCK'
        return 'ROCK'
    elif computer == 2:
        computer_choice_name = 'PAPER'
        return 'PAPER'
    else:
        computer_choice_name = 'SCISSORS'
        return 'SCISSORS'

# sets the rules for RPS game
def check_battle(computer, player):
    # Rock vs. Scissors: Rock wins.
    # Paper vs. Rock: Paper wins.
    # Scissors vs. Paper: Scissors wins.
    if computer == player:
        return "DRAW!"
    elif (computer == 3 and player == 1) or \
         (computer == 2 and player == 3) or (computer == 1 and player == 2):
        return "PLAYER"
    else:
        return "COMPUTER"

def main():
    # determine which team computer and user represent
    user_team = input("What team do you want(red or blue)?")
    if user_team.upper() == 'RED':
        user_team = 'RED'
        computer_team = 'BLUE'
    if user_team.upper() == 'BLUE':
        user_team = 'BLUE'
        computer_team = 'RED'
    # determine which random pokemon computer and player use
    num_user = random.randint(1, 10)
    get_player(num_user)
    num_computer = random.randint(1, 10)
    get_player(num_computer)
    print(f"{computer_team} {get_player(num_computer)}\
vs {user_team} {get_player(num_user)}")

    # count the score of user and computer
    user_score = 0
    computer_score = 0
    
    while True:
        game_no = 1
        # get computer's choice and player's input choice of game
        computer = random.randint(1, 3)
        computer_choice(computer)
        player = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors"))
        player_choice(player)
        print(f"{get_player(num_computer)} played {computer_choice(computer)}.\
{get_player(num_user)} played {player_choice(player)}")
        # check who wins the game, print the result, count the score
        check_battle(computer, player)
        if check_battle(computer, player) == "DRAW!":
            print("It's a draw! No winner")
        elif check_battle(computer, player) == "PLAYER":
            print(f"Your {user_team} team wins with {get_player(num_user)}!")
            user_score += 1
        else:
            print(f"My {computer_team} team wins \
with {get_player(num_computer)}!")
            computer_score += 1
        again = input("Play again (y/n)?")
        if again.lower() == 'y':
            game_no += 1
        else:
            break
        
    # game ends. prints the final results
    print(" Tournament has ended!")
    print(f" {user_team}:{user_score}     {computer_team}:{computer_score}")
    if user_score < computer_score:
        print(" I WIN!")
    elif user_score == computer_score:
        print(" DRAW! NO WINNER!")
    else:
        print(" YOU WIN!")

if __name__ == "__main__":
    main()
