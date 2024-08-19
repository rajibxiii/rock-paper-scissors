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

import random

choice = [rock, paper, scissors]
beatenBy = [paper, scissors, rock]

userChoiceIndex = int (input ("What do you want to choose?\nType 1 for Rock, 2 for Paper, or 3 for Scissors\n")) - 1
randomChoiceIndex = random.randint(0, 2)

print (f"\nYour choice: {choice [userChoiceIndex]}")
print (f"Computer's choice: {choice [randomChoiceIndex]}")

if userChoiceIndex == randomChoiceIndex:
    print ("It's a draw! 🤝") 
elif randomChoiceIndex == beatenBy.index(choice[userChoiceIndex]):
    print ("You win! 😊")
else:
    print ("Computer wins! 😓")
