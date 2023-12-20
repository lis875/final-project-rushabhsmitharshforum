#Story 2
import time
print("Welcome to the studio 1 adventure!")
name = input("Please tell me your name: ")
print("You are a Python programmer named", name, ". One day, you decide to go on an adventure.")
print("You find yourself at a crossroads.")
user_action = input("Do you want to go 'left' or 'right'? ")
if (user_action == "left" or user_action == "Left"):
    print("\nYou chose the left path and entered a dark forest.")
    print("You hear strange sounds and can't see much. What do you want to do? ")
    print("1. Keep walking deeper into the forest.")
    print("2. Turn back and take the right path.")
    user_choice = int(input("Tell me your choice 1 or 2? "))
    if (user_choice == 1):
        print("\nYou continue into the forest, but it gets darker and scarier. Suddenly, you are surrounded by wolves!")
        time.sleep(2)
        print("Oh no! The wolves attack you. Game over!")
    elif (user_choice == 2):
        print("\nYou wisely decide to turn back and take the right path.")
        print("\nYou chose the right path and start climbing a steep mountain.")
        print("After a challenging climb, you reach a cave.")
        user_choice1 = input("Do you want to 'enter' the cave or 'climb' further up the mountain? ")
        if (user_choice1 == "enter"):
            print("\nYou enter the cave and find a treasure chest full of Python code! You also discover a map.")
            print("The map leads you to a hidden Python village.")
            print("\nYou follow the map to the hidden Python village.")
            print("The villagers welcome you warmly and ask if you'd like to stay")
            user_choice2 = input("Do you want to 'stay' or 'leave' the village? ")
            if (user_choice2 == "stay"):
                print("\nYou decide to stay in the Python village and become a respected member of their community.")
                print("Congratulations! You've completed the Python Programmer's Adventure!")
            elif (user_choice2 == "leave"):
                print("\nYou bid farewell to the Python village and continue on your journey to explore more Pythonic adventures.")
            else:
                print("Oops, Sorry you gave the wrong input")
        elif (user_choice1 == "climb"):
            print("\nYou decide to climb higher, but it's getting too dangerous. Suddenly, you slip and fall. Game over!")
elif (user_action == "right" or user_action == "Right"):
    print("\nYou wisely decide to turn back and take the right path.")
    print("\nYou chose the right path and start climbing a steep mountain.")
    print("After a challenging climb, you reach a cave.")
    user_choice1 = input("Do you want to 'enter' the cave or 'climb' further up the mountain? ")
    if (user_choice1 == "enter"):
        print("\nYou enter the cave and find a treasure chest full of Python code! You also discover a map.")
        print("The map leads you to a hidden Python village.")
        print("\nYou follow the map to the hidden Python village.")
        print("The villagers welcome you warmly and ask if you'd like to stay")
        user_choice2 = input("Do you want to 'stay' or 'leave' the village? ")
        if (user_choice2 == "stay"):
            print("\nYou decide to stay in the Python village and become a respected member of their community.")
            print("Congratulations! You've completed the Python Programmer's Adventure!")
        elif (user_choice2 == "leave"):
            print("\nYou bid farewell to the Python village and continue on your journey to explore more Pythonic adventures.")
        else:
            print("Oops, Sorry you gave the wrong input")
    elif (user_choice1 == "climb"):
        print("\nYou decide to climb higher, but it's getting too dangerous. Suddenly, you slip and fall. Game over!")
else:
    print("Sorry you selected wrong input, Game Over!")