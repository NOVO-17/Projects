# This will be my actual first project name "Rock Paper and Sissors (loner edition) "
import random
def get_choices():
    player_choice =input("choose Rock, Paper and Sissors:")
    options = [ "rock", "paper", "sissors" ] 
    computer_choice = random.choice(options)
    choices={"player": player_choice, "computer": computer_choice}
    return choices
    
def check_win(player, computer):
    print(f"You chose {player} and computer chose {computer}")
    if player == computer:
        print("It's a tie!")
    
    elif player == "rock":
        if computer == "paper":
                return "Hah you lost, you couldn't even win against a computer loser!"
        else:
             return "You won!,But how much loner you are to play stone paper sissors with a computer ,SAD bro."

    elif player == "sissors":
        if computer == "rock":
                return "Hah you lost, you couldn't even win against a computer loser!"
        else:
             return "You won!,But how much loner you are to play stone paper sissors with a computer ,SAD bro."

    elif player == "paper":
        if computer == "sissors":
                return "Hah you lost, you couldn't even win against a computer loser!"
        else:
             return "You won!,But how much loner you are to play stone paper sissors with a computer ,SAD bro."

    else:
         print("can't type properly or what? loser...")
        
choices= get_choices()
result= check_win(choices["player"], choices["computer"])
print(result)