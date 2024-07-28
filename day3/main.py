# height = int(input("What is your height? "))
# if height >= 120:
#     age = int(input("Enter age: "))
#     if age <= 18:
#         print("Is not time yet")
#     elif age >=18: 
#         print("You can ride")
# else:
#     print("You cant ride")

# number = int(input("Enter number: "))
# if number%2==0:
#     print("int")
# else:
#     print("not int")

# pizza maker

# dollars = 100

# print("Congratulations! You was invited to job a pizza maker\n")
# print("MENU")
# print("----------------------------------------------------------")
# print("Small Pizza. 15$. Enter S")
# print("Medium Pizza. 30$. Enter M")
# print("Large Pizza. 50$. Enter L")
# print("----------------------------------------------------------")

# choose = input("Choose: ")
# if choose == "S":
#     dollars -= 15
#     print(f"You choose: Small Pizza. Dollars haves: {dollars}")
# elif choose == "M":
#     dollars -= 30
#     print(f"You choose: Medium Pizza. Dollars haves: {dollars}")
# elif choose == "L":
#     dollars -= 50
#     print(f"You choose: Large Pizza. Dollars haves: {dollars}")

# Game

print("Welcome to Treasure Island. Your mission is to find the treasure.")
path = str(input("Input LEFT or RIGTH to move by character. "))
if path == "RIGHT":
    print("Game Over!")
elif path == "LEFT":
    action = str(input("SWIM or WAIT? "))
    if action == "SWIM":
        print("Game Over!")
    elif action == "WAIT":
        door = str(input("Which door? RED or BLUE or maybe YELLOW? "))
        if door == "RED":
            print("Game Over!")
        elif door == "BLUE":
            print("Game Over!")
        elif door == "YELLOW":
            print("YOU WIN!!!!")


