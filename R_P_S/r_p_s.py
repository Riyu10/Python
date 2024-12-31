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

choice = int(input("Choose: 0 for Rock, 1 for Paper, 2 for Scissors"))
if choice == 0:
    print(f"You: \n{rock}")
elif choice == 1:
    print(f"You: \n{paper}")
else:
    print(f"You: \n{scissors}")
comp = random.randint(0, 2)
if comp == 0:
    print(f"Computer: \n{rock}")
elif comp == 1:
    print(f"Computer: \n{paper}")
else:
    print(f"Computer: \n{scissors}")