from turtle import *
import time
penup()
setposition(-600, 300)
pendown()

def introduction():
    write("Welcome to Lila's Enchanted Forest Adventure!")
    move_next()
    write("In this story, you will guide Lila through an enchanted forest filled with mysteries and wonders.")
    move_next()
    write("Your choices will shape her journey. Let's begin!")
    move_next()
    # Insert the introduction image here

def enter_forest():
    write("\nLila stands at the edge of the enchanted forest, filled with curiosity and excitement.")
    move_next()
    # Insert the image of Lila at the forest's edge here
    return make_choice("Does Lila enter the forest or stay back? Type 'enter' or 'stay': ", ['enter', 'stay', 'quit'])

def forest_decision():
    write("\nUpon entering the forest, Lila finds an ancient, moss-covered stone well.")
    move_next()
    # Insert the image of the ancient well here
    return make_choice("Does she climb down the well or explore around? Type 'climb' or 'explore': ", ['climb', 'explore', 'quit'])

def underground_world():
    write("\nDescending into the well, Lila discovers a luminous underground world.")
    move_next()
    # Insert the image of the underground world here
    return make_choice("Does she seek the treasure or return to the surface? Type 'seek' or 'return': ", ['seek', 'return', 'quit'])

def hidden_grove():
    write("\nExploring around, Lila discovers a hidden grove with a talking tree.")
    move_next()
    # Insert the image of the hidden grove here
    return make_choice("Does she investigate the tree or head back? Type 'investigate' or 'back': ", ['investigate', 'back', 'quit'])

def conclusion():
    write("\nAfter her adventures, Lila learns the value of curiosity, bravery, and the comfort of home.")
    move_next()
    write("She returns home, her heart filled with unforgettable memories and dreams of future adventures.")
    move_next()
    # Insert the conclusion image here

def quit_story():
    write("Thank you for your time, Good Bye, See You!")
    move_next()

def move_next():
    penup()
    right(90)
    forward(30)
    left(90)
    pendown()

def make_choice(prompt, options):
    choice = textinput("Title", prompt)
    while choice not in options:
        write("Invalid choice. Please try again.")
        choice = input(prompt).lower()
    return choice


introduction()

decision = enter_forest()


if decision == "enter":
    decision = forest_decision()

    if decision == "climb":
        decision = underground_world()

        
        if decision == "seek":
            write("\nBraving the challenges, Lila finds a hidden treasure and learns about courage and determination.")
            move_next()
        elif decision == "quit":
            decision = quit_story()
            # Insert an image related to the treasure discovery here
        else:
            write("\nLila finds her way back to the surface, encountering beautiful and mystical sights.")
            move_next()
            # Insert an image of Lila's return to the surface here

    elif decision == "quit":
        decision = quit_story()

    else:
        decision = hidden_grove()
       
        if decision == "investigate":
            write("\nIn the grove, Lila uncovers secrets about the forest and gains wisdom from the talking tree.")
            move_next()
            # Insert an image related to the talking tree here
        elif decision == "quit":
            decision = quit_story()
        else:
            write("\nLila decides to return to the forest path, ready for new adventures.")
            move_next()
            # Insert an image of Lila on a new path here

elif decision == "quit":
    conclusion()
    decision = quit_story()

else:
    write("\nChoosing to stay back, Lila finds a mysterious map in her attic, hinting at future adventures.")
    move_next()
    # Insert an image of Lila finding the map here
# conclusion()
done()