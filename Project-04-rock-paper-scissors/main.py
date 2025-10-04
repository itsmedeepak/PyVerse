#from curses.ascii import isdigit
import random

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
game_images = [rock, paper, scissors]

while True:
  print("Type 0 for Rock, 1 for Paper or 2 for Scissors. and q to quit the game.")
  chosen_opt=input("What do you choose? \n")
  if chosen_opt.isdigit() and int(chosen_opt) in range(0,3):
    user_choice = int(chosen_opt)
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0: 
      print("You typed an invalid number, you lose!") 
    elif user_choice == 0 and computer_choice == 2:
      print("You win!")
    elif computer_choice == 0 and user_choice == 2:
      print("You lose")
    elif computer_choice > user_choice:
      print("You lose")
    elif user_choice > computer_choice:
      print("You win!")
    elif computer_choice == user_choice:
      print("It's a draw")
  elif chosen_opt.lower()=='q':
    print("Quiting..")
    break
    quit()
  else:
    print("please make valid selection.")

