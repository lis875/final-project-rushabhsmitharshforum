from turtle import *
import time

def introduction():
    print("Welcome to Lila's Enchanted Forest Adventure!")
    print("In this story, you will guide Lila through an enchanted forest filled with mysteries and wonders.")
    print("Your choices will shape her journey. Let's begin!")
    # Insert the introduction image here

def enter_forest():
    print("\nLila stands at the edge of the enchanted forest, filled with curiosity and excitement.")
    # Insert the image of Lila at the forest's edge here
    return make_choice("Does Lila enter the forest or stay back? Type 'enter' or 'stay': ", ['enter', 'stay'])

def forest_decision():
    print("\nUpon entering the forest, Lila finds an ancient, moss-covered stone well.")
    # Insert the image of the ancient well here
    return make_choice("Does she climb down the well or explore around? Type 'climb' or 'explore': ", ['climb', 'explore'])

def underground_world():
    print("\nDescending into the well, Lila discovers a luminous underground world.")
    # Insert the image of the underground world here
    return make_choice("Does she seek the treasure or return to the surface? Type 'seek' or 'return': ", ['seek', 'return'])

def hidden_grove():
    print("\nExploring around, Lila discovers a hidden grove with a talking tree.")
    # Insert the image of the hidden grove here
    return make_choice("Does she investigate the tree or head back? Type 'investigate' or 'back': ", ['investigate', 'back'])

def conclusion():
    print("\nAfter her adventures, Lila learns the value of curiosity, bravery, and the comfort of home.")
    print("She returns home, her heart filled with unforgettable memories and dreams of future adventures.")
    # Insert the conclusion image here

def make_choice(prompt, options):
    choice = textinput(prompt, "Your choice: ")
    while choice not in options:
        print("Invalid choice. Please try again.")
        choice = input(prompt).lower()
    return choice

introduction()

decision = enter_forest()

if decision == "enter":
    decision = forest_decision()

    if decision == "climb":
        decision = underground_world()
        if decision == "seek":
            print("\nBraving the challenges, Lila finds a hidden treasure and learns about courage and determination.")
            # Insert an image related to the treasure discovery here
        else:
            print("\nLila finds her way back to the surface, encountering beautiful and mystical sights.")
            # Insert an image of Lila's return to the surface here

    else:
        decision = hidden_grove()
        if decision == "investigate":
            print("\nIn the grove, Lila uncovers secrets about the forest and gains wisdom from the talking tree.")
            # Insert an image related to the talking tree here
        else:
            print("\nLila decides to return to the forest path, ready for new adventures.")
            # Insert an image of Lila on a new path here

else:
    print("\nChoosing to stay back, Lila finds a mysterious map in her attic, hinting at future adventures.")
    # Insert an image of Lila finding the map here

conclusion()