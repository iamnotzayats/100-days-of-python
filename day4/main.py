import random as r
# random_integer = r.randint(1,10)
# print(random_integer)

# region_of_russia = ["Татарстан", "Кемеровская область", "Республика Крым", "Белгородская область"]
# Добавляет новый обьект
# region_of_russia.append("Республика Ингушетия")
# print(region_of_russia)

# names = ["Владик"]
# items = len(names)
# print("Кто будет платить завтра в кальянной?")
# random_choise = r.randint(0, items-1)
# print(names[random_choise])


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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
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