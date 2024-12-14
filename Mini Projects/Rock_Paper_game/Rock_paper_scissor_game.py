"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
"""

import random
item_list = ["Rock", "Paper", "Scissor"]

#Input
user_name = input("Enter your name: ")
user_choice = input("Enter your move = Rock, Paper, Scissor = ")
Computer_choice = random.choice(item_list)

#print
print(f"User choice = {user_choice} \nComputer choice = {Computer_choice}")

# Cases
if user_choice == Computer_choice:
    print("Both choose same:  = Match Tie")

elif(user_choice == "Rock"):
    if(Computer_choice == "Paper"):
        print("Paper covers Rock = Computer Win")
    else:
        print(f"Rock smashes scissor = {user_name} Win")

elif(user_choice == "Paper"):
    if(Computer_choice == "Scissor"):
        print("Scissor cuts paper = Computer Win")
    else:
        print("Paper covers rock = {user_name} Win")

elif(user_choice == "Scissor"):
    if(Computer_choice == "Paper"):
        print("Scissor cuts paper = {user_name} Win")
    else:
        print("Rock smashes scissor = Computer Win")