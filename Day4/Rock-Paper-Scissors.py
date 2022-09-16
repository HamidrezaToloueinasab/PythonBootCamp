# Rock Paper Scissors 
import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

Game = [Rock, Paper, Scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if player_choice >= 3 or player_choice < 0:
    print("You Typed an invalid number, You Lose!")
else:
    print(Game[player_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(Game[computer_choice])

    if player_choice == 0 and computer_choice ==2:
        print("You Win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You Lose!")
    elif computer_choice > player_choice:
        print("You Lose!")
    elif player_choice > computer_choice:
        print("You Win!")
    elif computer_choice == player_choice:
        print("It's a draw!")