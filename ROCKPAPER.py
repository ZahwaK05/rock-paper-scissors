import random
def rock_paper_scissors():
    def welcome():
        print("Welcome to Rock, Paper, Scissors!")
        print("Please choose one of the following options:")
        print("1. Rock 🪨")
        print("2. Paper 📃")
        print("3. Scissors ✂️")
    def get_computer_choice():
        computer=random.choice(['rock', 'paper', 'scissors'])
        return computer
    def determine_winner(player,computer):
        if player== computer:
            return "It's a tie!"
        elif (player=='rock' and computer=='scissors') or (player=='paper' and computer=='rock') or (player=='scissors' and computer=='paper'):
            return "You win!"
        else:
            return "Computer wins!"
    welcome()
    computer_choice=get_computer_choice()
    player=input("Enter your choice (1-3): ")
    if player=='1':
        player='rock'
    elif player=='2':
        player='paper'
    elif player=='3':
        player='scissors'
    print(f"You chose: {player}")
    print(f"Computer chose: {computer_choice}")         
    result=determine_winner(player, computer_choice)
    print(result)


def rock_paper_scissors_lizard_spock():
    def welcome():
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("Please choose one of the following options:")
        print("1. Rock 🪨")
        print("2. Paper 📃")
        print("3. Scissors ✂️")
        print("4. Lizard 🦎")
        print("5. Spock 🖖")
    def get_computer_choice():
        computer=random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])
        return computer
    def determine_winner(player,computer):
        if player== computer:
            return "It's a tie!"
        elif (player=='rock' and (computer=='scissors' or computer=='lizard')) or (player=='paper' and (computer=='rock' or computer=='spock')) or (player=='scissors' and (computer=='paper' or computer=='lizard')) or (player=='lizard' and (computer=='spock' or computer=='paper')) or (player=='spock' and (computer=='scissors' or computer=='rock')):
            return "You win!"
        else:
            return "Computer wins!"
    welcome()
    computer_choice=get_computer_choice()
    player=input("Enter your choice (1-5): ")
    if player=='1':
        player='rock'
    elif player=='2':
        player='paper'
    elif player=='3':
        player='scissors'
    elif player=='4':
        player='lizard'
    elif player=='5':
        player='spock'
    print(f"You chose: {player}")
    print(f"Computer chose: {computer_choice}")         
    result=determine_winner(player, computer_choice)
    print(result)
print("Welcome,Choose a game mode:")
print("1. Rock, Paper, Scissors")
print("2. Rock, Paper, Scissors, Lizard, Spock")
mode=input("Enter your choice (1-2): ")
if mode=='1':
    rock_paper_scissors()
elif mode=='2':
    rock_paper_scissors_lizard_spock()
else:
    print("Invalid choice.")
 