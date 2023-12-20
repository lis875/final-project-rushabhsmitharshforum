from turtle import *
import turtle
import winsound
import sys

screen = turtle.Screen()
# import Passcode
bgcolor("#1F3E5B")
color("#C6C1C1")

winsound.PlaySound("song.wav",winsound.SND_ASYNC)

def passcode():
    screen.addshape("Img_Stealing.gif")
    image_turtle = turtle.Turtle()
    image_turtle.shape("Img_Stealing.gif")
    image_turtle.penup()
    image_turtle.goto(460,100)
    write("Suspect is trying to enter the Passcode", font=style1)    
    passcode_input = textinput("Enter the Passcode to open Safe","Enter the Independance Day of America")
    if(passcode_input == "1776"):
        screen.addshape("Img_Sptlight.gif")
        image_turtle = turtle.Turtle()
        image_turtle.shape("Img_Sptlight.gif")
        image_turtle.penup()
        image_turtle.goto(460,100)
        move_next()
        write("Jewel is stolen", font=style1)    
        resultt()
        move_next()
    else:
        screen.addshape("Img_Sptlight.gif")
        image_turtle = turtle.Turtle()
        image_turtle.shape("Img_Sptlight.gif")
        image_turtle.penup()
        image_turtle.goto(460,100)
        move_next()
        write("Intruder Alert! The siren goes on", font=style1)    
        resultt()
        move_next()


speed(0)
penup()
setposition(-630, 280)
pendown()
style = ('Arial', 25)
style1 = ('Arial', 13)
def introduction():
    write("The London Jewel Heist: A Sherlock Holmes Adventure", font=style)
    move_next()
    write("In the heart of London, where the fog clings to the Cobblestone streets, Sherlock Holmers and Dr. Watson", font=style1)
    move_next()
    write("receive an urgent summons from Buckingham Palace. Queen Victoria, concerned about rumors of a planned heist during", font=style1)
    move_next()
    write("her grand birthday celebration, requested their discreet assistance. The target: A Priceless Royal Jewel", font=style1)
    move_next()
    # image = "C:\Users\forum\Desktop\LIS875\FinalProject\final-project-rushabhsmitharshforum\final-project-rushabhsmitharshforum\Start_1.png"
    
    screen.addshape("Intro_1.gif")
    image_turtle = turtle.Turtle()
    image_turtle.shape("Intro_1.gif")
    image_turtle.penup()
    image_turtle.goto(460,100)
    # win.setup(width = 500, height = 1200)  
    # win.bgpic('Intro_1.gif')
    # turtle.mainloop()
    # Insert the introduction image here

def sherlock_decision():
    # Insert the image of Lila at the forest's edge here
    
    return make_choice("Sherlock: Watson shall we embark on this royal endeavor?" , ['yes', 'quit'])
    

def security():
    write("Under the shadow of royal portraits and the echoes of past intrigues, Sherlock and Watson explore methods to protect jewel.", font=style1)
    return make_choice("How should they secure the jewel?\na. Increase the number of bodyguards\nb. Implement stringent security checks for all attendees\nc. Disguise police officers as civilians among the guests" , ['a', 'b', 'c', 'quit'])

def suspects():
    move_next()
    write("On the eve of queens birthday, the palace is a flurry of activity. Three individuals catch sherlock's analytical eyes.", font=style1)
    move_next()
    write("Suspect1: The Bartender (Sir Reginald)", font=style1)
    move_next()
    write("Suspection reason: Oddly inexperienced yet chosen for this prestegious event, More observant of guests than attentive ", font=style1)
    move_next()
    write("to his duties, Frequent unexplained absences", font=style1)
    move_next()
    write("Suspect2: The Butler (Count Wilfred)", font=style1)
    move_next()
    write("Suspection reason: Unfettered access throughout the palace, A long-serving employee living modestly", font=style1)
    move_next()
    write("Suspect3: The Step-Nephew (Peter Windsor)", font=style1)
    move_next()
    write("Suspection reason: Bitter about his exclusion from royal priviliges, Desires to disrupt the line of succession", font=style1)
    move_next()
    write("The suspect tries to infiltrate the inner sanctum with omnious intent", font=style1)
    # Insert the image of the underground world here

def security_check():
    move_next()
    write("Suspect is trying to enter the palace, and he is stopped for security check", font=style1)
    return make_choice("Do you want suspects to be caught? Yes or No", ["yes", "no"])

def suspect_weapon():
    # Insert the image of the hidden grove here
    return make_choice("What weapon do you want suspect to carry in the party: (Knife, Poison or Gun)", ['knife', 'poison', 'gun'])

def resultt():
    move_next()
    write("The focus of the light was on the suspect in the room", font=style1)
    move_next()
    write("Sherlock: CHECKMATE!", font=style1)
    move_next()


def culprit_caught_knife():
    write("The party was going on very smoothly, suddenly there was a  power cut, everyone  started panicking, except Sherlock.", font=style1)
    move_next()
    write("By taking advantage of the power cutoff, the susoect tried to sneak into the royal room to steal the royal jewel", font=style1)
    move_next()
    write("soon as suspect tried to run from the royal room", font=style1)
    move_next()
    write("to steal the royal diamond, soon as suspect tried to run from the royal room", font=style1)
    move_next()
    passcode()
    move_next()
    
    write("The lights in the palace were restored immediately, sherlock bought the culprit in front of the queen, the diamond was still in the hand of the culprit, sherlock said in", font=style1)
    move_next()
    write("front of everyone that the diamond is fake and real diamond is safe, everyone was shocked and started murmuring and thinking about where the real diamond is.", font=style1)

def culprit_caught_poison():
    write("The party was going on very smoothly, everyone was having food and enjoying their drinks, suddenly everyone started to faint,", font=style1)
    move_next()
    write("except Sherlock, Dr. Watson and The Queen", font=style1)
    move_next()
    write("but they also pretended to faint. After some time everyone in the party fainted, the suspect tried to sneak into the royal room to steal the diamond,", font=style1)
    move_next()
    write("soon as suspect tried to run from the royal room", font=style1)
    move_next()
    write("to steal the royal diamond, soon as suspect tried to run from the royal room", font=style1)
    move_next()
    
    passcode()

    move_next()
    
    write("Soon after sometime everyone became conscious, sherlock bought the culprit in front of the queen, the diamond was still in the hand of the culprit, sherlock said in front of everyone that the diamond is fake and", font=style1)
    move_next()
    write("real diamond is safe, everyone was shocked and started murmuring and thinking about where the real diamond is", font=style1)

def culprit_caught_gun():
    write("The party was going on very smoothly, suddenly there was a  power cut, everyone  started panicking, except Sherlock.", font=style1)
    move_next()
    write("By taking advantage of the power cutoff, the suspect tried to sneak into the royal room to steal the royal jewel,", font=style1)
    move_next()
    write("soon as suspect tried to run from the royal room", font=style1)
    move_next()
    write("to steal the royal diamond, soon as suspect tried to run from the royal room", font=style1)
    move_next()
    
    passcode()
    move_next()
    
    write("The lights in the palace were restored immediately, sherlock bought the culprit in front of the queen, the diamond was still in the hand of the culprit, sherlock said in", font=style1)
    move_next()
    write("front of everyone that the diamond is fake and real diamond is safe, everyone was shocked and started murmuring and thinking about where the real diamond is.", font=style1)

def culprit_guess():
    winsound.PlaySound("song.wav",winsound.SND_ASYNC)
    return make_choice("Can you guess who was the culprit? (bartender, butler or nephew)", ['bartender', 'butler', 'nephew'])

def diamond_guess():
    return make_choice("Can you guess where the real diamond is? (Saferoom or Queen's Crown)", ['saferoom', 'crown'])

# def conclusion():
#     write("\nAfter her adventures, Lila learns the value of curiosity, bravery, and the comfort of home.")
#     move_next()
#     write("She returns home, her heart filled with unforgettable memories and dreams of future adventures.")
#     move_next()
    # Insert the conclusion image here

def quit_story():
    write("Thank you for your time, Good Bye, See You!")
    move_next()

def move_next():
    penup()
    right(90)
    forward(18)
    left(90)
    pendown()

def make_choice(prompt, options):
    choice = textinput("Title", prompt)
    while choice not in options:
        write("Invalid choice. Please try again.")
        choice = input(prompt).lower()
    return choice


introduction()
def crown_final():
    decision = diamond_guess()
    if decision == 'crown':
        move_next()
        write("Yes, you guessed it correct", font=style1)
        screen.addshape("Img_End.gif")
        image_turtle = turtle.Turtle()
        image_turtle.shape("Img_End.gif")
        image_turtle.penup()
        image_turtle.goto(460,100)
    elif decision == 'saferoom':
        move_next()
        write("No, the correct option is queen's crown", font=style1)
        screen.addshape("Img_End.gif")
        image_turtle = turtle.Turtle()
        image_turtle.shape("Img_End.gif")
        image_turtle.penup()
        image_turtle.goto(460,100)

decision = sherlock_decision()
if decision == "yes":
    screen.addshape("Img_Palace_Ext.gif")
    image_turtle = turtle.Turtle()
    image_turtle.shape("Img_Palace_Ext.gif")
    image_turtle.penup()
    image_turtle.goto(460,100)
    decision = security()
    if decision == "a":
        move_next()
        write("Okay number of bodyguards were increased", font=style1)
        screen.addshape("Img_Inside1.gif")
        image_turtle = turtle.Turtle()
        image_turtle.shape("Img_Inside1.gif")
        image_turtle.penup()
        image_turtle.goto(460,100)

    elif decision == "b":
        move_next()
        write("Okay, srtigent security check for all the attendees has been implemented", font=style1)
        screen.addshape("Img_Inside1.gif")
        image_turtle = turtle.Turtle()
        image_turtle.shape("Img_Inside1.gif")
        image_turtle.penup()
        image_turtle.goto(460,100)
    elif decision == "c":
        move_next()
        write("Okay, police officers were disguised as civilians amonng the guest", font=style1)
        screen.addshape("Img_Inside1.gif")
        image_turtle = turtle.Turtle()
        image_turtle.shape("Img_Inside1.gif")
        image_turtle.penup()
        image_turtle.goto(460,100)

    suspects()
    decision = security_check()
    if decision == 'yes':
        move_next()
        write("Suspect was a friend of police officer, he let him through the security check", font=style1)
        decision = suspect_weapon()  # Assign the result of suspect_weapon() to decision
        if decision == 'knife':
            screen.addshape("Img_Nxt_Knife.gif")
            image_turtle = turtle.Turtle()
            image_turtle.shape("Img_Nxt_Knife.gif")
            image_turtle.penup()
            image_turtle.goto(460,100)
            move_next()
            culprit_caught_knife()
            decision = culprit_guess()
            if decision == 'bartender':
                screen.addshape("Img_Nxt_Knife.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_Nxt_Knife.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("Yes correct choice", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()
            elif decision == 'butler' or 'nephew':
                screen.addshape("Img_caught.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_caught.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("No, since the weapon is knife and bartender continuously used to visit the electricity room, he tried to cut the wired with knife, hence the culprit is Bartender", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()

        elif decision == 'poison':
            screen.addshape("Img_Poison.gif")
            image_turtle = turtle.Turtle()
            image_turtle.shape("Img_Poison.gif")
            image_turtle.penup()
            image_turtle.goto(460,100)
            move_next()
            culprit_caught_poison()
            decision = culprit_guess()
            if decision == 'butler':
                screen.addshape("Img_Poison.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_Poison.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("Yes correct choice", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()
            elif decision == 'bartender' or 'nephew':
                screen.addshape("Img_caught.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_caught.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("No, since the weapon is poison and butler was working in the palace for several years, he knew each and every corner of the palace. Since everyone fainted after having food, it was obvious that the butler added the poison in the food", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()

        elif decision == 'gun':
            screen.addshape("Img_Nxt_Gun.gif")
            image_turtle = turtle.Turtle()
            image_turtle.shape("Img_Nxt_Gun.gif")
            image_turtle.penup()
            image_turtle.goto(460,100)
            move_next()
            culprit_caught_gun()
            decision = culprit_guess()
            if decision == 'nephew':
                screen.addshape("Img_caught.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_caught.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("Yes correct choice", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()
            elif decision == 'butler' or 'bartender':
                screen.addshape("Img_caught.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_caught.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("No, since the weapon is gun and all the family members were ashamed of the action that one of their family member tried to steal the diamond", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()

    elif decision == 'no':
        move_next()
        write("Suspect was a friend of police officer, he let him through the security check", font=style1)
        decision = suspect_weapon()  # Assign the result of suspect_weapon() to decision
        if decision == 'knife':
            move_next()
            culprit_caught_knife()
            decision = culprit_guess()
            if decision == 'bartender':
                screen.addshape("Img_Nxt_Knife.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_Nxt_Knife.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("Yes correct choice", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()
            elif decision == 'butler' or 'nephew':
                screen.addshape("Img_caught.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_caught.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("No, since the weapon is knife and bartender continuously used to visit the electricity room, he tried to cut the wired with knife, hence the culprit is Bartender", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                decision = diamond_guess()
                if decision == 'crown':
                    move_next()
                    write("Yes, you guessed it correct", font=style1)
                elif decision == 'saferoom':
                    move_next()
                    write("No, the correct option is queen's crown, font=style1")

        elif decision == 'poison':
            screen.addshape("Img_Poison.gif")
            image_turtle = turtle.Turtle()
            image_turtle.shape("Img_Poison.gif")
            image_turtle.penup()
            image_turtle.goto(460,100)
            move_next()
            culprit_caught_poison()
            decision = culprit_guess()
            if decision == 'butler':
                screen.addshape("Img_caught.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_caught.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("Yes correct choice", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()
            elif decision == 'bartender' or 'nephew':
                screen.addshape("Img_caught.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_Palace_Ext.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("No, since the weapon is poison and butler was working in the palace for several years, he knew each and every corner of the palace. Since everyone fainted after having food, it was obvious that the butler added the poison in the food", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()

        elif decision == 'gun':
            screen.addshape("Img_Nxt_Gun.gif")
            image_turtle = turtle.Turtle()
            image_turtle.shape("Img_Nxt_Gun.gif")
            image_turtle.penup()
            image_turtle.goto(460,100)
            move_next()
            culprit_caught_gun()
            decision = culprit_guess()
            if decision == 'nephew':
                screen.addshape("Img_caught.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_caught.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("Yes correct choice", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()
            elif decision == 'butler' or 'bartender':
                screen.addshape("Img_caught.gif")
                image_turtle = turtle.Turtle()
                image_turtle.shape("Img_caught.gif")
                image_turtle.penup()
                image_turtle.goto(460,100)
                move_next()
                write("No, since the weapon is gun and all the family members were ashamed of the action that one of their family member tried to steal the diamond", font=style1)
                move_next()
                write("The Queen sentenced the culprit to jail", font=style1)
                crown_final()

        if decision == 'bartender':
            move_next()
            write("Yes correct choice", font=style1)
            move_next()
            write("The Queen sentenced the culprit to jail", font=style1)
            decision == diamond_guess()
            if decision == 'crown':
                write("Yes, you guessed it correct", font=style1)
            elif decision == 'saferoom':
                write("No, the correct option is queen's crown", font=style1)
    # elif decision == "quit":
    #     decision = quit_story()
            # Insert an image related to the treasure discovery here
    # else:
    #     write("\nLila finds her way back to the surface, encountering beautiful and mystical sights.")
    #     move_next()
            # Insert an image of Lila's return to the surface here

# elif decision == "quit":
#     decision = quit_story()
done()