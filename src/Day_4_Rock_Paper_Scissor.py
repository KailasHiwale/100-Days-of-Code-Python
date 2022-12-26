# project 4: Rock, Paper, Scissor Game
"""Write a program for Rock, Paper and Scissors game.
Four simple rules:
1. Rock wins against scissors.
2. Scissors win against paper.
3. Paper wins against rock."""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice >= 3 or user_choice < 0:
  print("You chose invalid option, you lose!")
else:
  print(game_images[user_choice])
  computer_choice = random.randint(0, 2)
  print("Computer chose: ")
  print(game_images[computer_choice])
  if user_choice == computer_choice:
    print("Its a draw!")
  elif user_choice == 0:
    if computer_choice == 1:
      print("You lose!")
    else:
      print("You win!")
  elif user_choice == 1:
    if computer_choice == 2:
      print("You lose!")
    else:
      print("You win!")
  else:
    if computer_choice == 0:
      print("You lose!")
    else:
      print("You win!")
  
  

