from turtle import *
speed(0)
penup()
setposition(-600, 300)
pendown()

def introduction():
    write("The London Jewel Heist: A Sherlock Holmes Adventure")
    move_next()
    write("In the heart of London, where the fog clings to the Cobblestone streets, Sherlock Holmers and Dr. Watson")
    move_next()
    write("receive an urgent summons from Buckingham Palace. Queen Victoria, concerned about rumors of a planned heist during")
    move_next()
    write("her grand birthday celebration, requested their discreet assistance. The target: A Priceless Royal Jewel")
    move_next()
    # Insert the introduction image here

def sherlock_decision():
    # Insert the image of Lila at the forest's edge here
    return make_choice("Sherlock: Watson shall we embark on this royal endeavor?" , ['yes', 'quit'])

def security():
    write("Under the shadow of royal portraits and the echoes of past intrigues, Sherlock and Watson explore methods to protect the jewel.")
    return make_choice("How should they secure the jewel?\na. Increase the number of bodyguards\nb. Implement stringent security checks for all attendees\nc. Disguise police officers as civilians among the guests" , ['a', 'b', 'c', 'quit'])

def suspects():
    move_next()
    write("On the eve of queens birthday, the palace is a flurry of activity. Three individuals catch sherlock's analytical eyes.")
    move_next()
    write("Suspect1: The Bartender (Sir Reginald)")
    move_next()
    write("Suspection reason: Oddly inexperienced yet chosen for this prestegious event, More observant of guests than attentive to his duties, Frequent unexplained absences")
    move_next()
    write("Suspect2: The Butler (Count Wilfred)")
    move_next()
    write("Suspection reason: Unfettered access throughout the palace, A long-serving employee living modestly")
    move_next()
    write("Suspect3: The Step-Nephew (Peter Windsor)")
    move_next()
    write("Suspection reason: Bitter about his exclusion from royal priviliges, Desires to disrupt the line of succession")
    move_next()
    write("The suspect tries to infiltrate the inner sanctum with omnious intent")
    # Insert the image of the underground world here

def security_check():
    move_next()
    write("Suspect is trying to enter the palace, and he is stopped for security check")
    return make_choice("Do you want suspects to be caught? Yes or No", ["yes", "no"])

def suspect_weapon():
    # Insert the image of the hidden grove here
    return make_choice("What weapon do you want suspect to carry in the party: (Knife, Poison or Gun)", ['knife', 'poison', 'gun'])

def culprit_caught_knife():
    write("The party was going on very smoothly, suddenly there was a  power cut, everyone  started panicking, except Sherlock.")
    move_next()
    write("By taking advantage of the power cutoff, the susoect tried to sneak into the royal room to steal the royal jewel, soon as suspect tried to run from the royal room")
    move_next()
    write("to steal the royal diamond, soon as suspect tried to run from the royal room")
    move_next()
    write("The focus of the light was on the suspect in the room")
    move_next()
    write("Sherlock: CHECKMATE!")
    move_next()
    write("The lights in the palace were restored immediately, sherlock bought the culprit in front of the queen, the diamond was still in the hand of the culprit, sherlock said in")
    move_next()
    write("front of everyone that the diamond is fake and real diamond is safe, everyone was shocked and started murmuring and thinking about where the real diamond is.")

def culprit_caught_poison():
    write("The party was going on very smoothly, everyone was having food and enjoying their drinks, suddenly everyone started to faint, except Sherlock, Dr. Watson and The Queen")
    move_next()
    write("but they also pretended to faint. After some time everyone in the party fainted, the suspect tried to sneak into the royal room to steal the diamond, soon as suspect tried to run from the royal room")
    move_next()
    write("to steal the royal diamond, soon as suspect tried to run from the royal room")
    move_next()
    write("The focus of the light was on the suspect in the room")
    move_next()
    write("Sherlock: CHECKMATE!")
    move_next()
    write("Soon after sometime everyone became conscious, sherlock bought the culprit in front of the queen, the diamond was still in the hand of the culprit, sherlock said in front of everyone that the diamond is fake and")
    move_next()
    write("real diamond is safe, everyone was shocked and started murmuring and thinking about where the real diamond is")

def culprit_caught_gun():
    write("The party was going on very smoothly, suddenly there was a  power cut, everyone  started panicking, except Sherlock.")
    move_next()
    write("By taking advantage of the power cutoff, the susoect tried to sneak into the royal room to steal the royal jewel, soon as suspect tried to run from the royal room")
    move_next()
    write("to steal the royal diamond, soon as suspect tried to run from the royal room")
    move_next()
    write("The focus of the light was on the suspect in the room")
    move_next()
    write("Sherlock: CHECKMATE!")
    move_next()
    write("The lights in the palace were restored immediately, sherlock bought the culprit in front of the queen, the diamond was still in the hand of the culprit, sherlock said in")
    move_next()
    write("front of everyone that the diamond is fake and real diamond is safe, everyone was shocked and started murmuring and thinking about where the real diamond is.")

def culprit_guess():
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
    forward(10)
    left(90)
    pendown()

def make_choice(prompt, options):
    choice = textinput("Title", prompt)
    while choice not in options:
        write("Invalid choice. Please try again.")
        choice = input(prompt).lower()
    return choice


introduction()

decision = sherlock_decision()
if decision == "yes":
    decision = security()
    if decision == "a":
        move_next()
        write("Okay number of bodyguards were increased")
    elif decision == "b":
        move_next()
        write("Okay, srtigent security check for all the attendees has been implemented")
    elif decision == "c":
        move_next()
        write("Okay, police officers were disguised as civilians amonng the guest")

    suspects()
    decision = security_check()
    if decision == 'yes':
        move_next()
        write("Suspect was a friend of police officer, he let him through the security check")
        decision = suspect_weapon()  # Assign the result of suspect_weapon() to decision
        if decision == 'knife':
            move_next()
            culprit_caught_knife()
            decision = culprit_guess()
            if decision == 'bartender':
                move_next()
                write("Yes correct choice")
            elif decision == 'butler' or 'nephew':
                move_next()
                write("No, since the weapon is knife and bartender continuously used to visit the electricity room, he tried to cut the wired with knife, hence the culprit is Bartender")
                move_next()
                write("The Queen sentenced the culprit to jail")
                decision = diamond_guess()
                if decision == 'crown':
                    move_next()
                    write("Yes, you guessed it correct")
                elif decision == 'saferoom':
                    move_next()
                    write("No, the correct option is queen's crown")

        elif decision == 'poison':
            move_next()
            culprit_caught_poison()
            decision = culprit_guess()
            if decision == 'butler':
                move_next()
                write("Yes correct choice")
            elif decision == 'bartender' or 'nephew':
                move_next()
                write("No, since the weapon is poison and butler was working in the palace for several years, he knew each and every corner of the palace. Since everyone fainted after having food, it was obvious that the butler added the poison in the food")
                move_next()
                write("The Queen sentenced the culprit to jail")
                decision = diamond_guess()
                if decision == 'crown':
                    move_next()
                    write("Yes, you guessed it correct")
                elif decision == 'saferoom':
                    move_next()
                    write("No, the correct option is queen's crown")

        elif decision == 'gun':
            move_next()
            culprit_caught_gun()
            decision = culprit_guess()
            if decision == 'nephew':
                move_next()
                write("Yes correct choice")
            elif decision == 'butler' or 'bartender':
                move_next()
                write("No, since the weapon is knife and bartender continuously used to visit the electricity room, he tried to cut the wired with knife, hence the culprit is Bartender")
                move_next()
                write("The Queen sentenced the culprit to jail")
                decision = diamond_guess()
                if decision == 'crown':
                    move_next()
                    write("Yes, you guessed it correct")
                elif decision == 'saferoom':
                    move_next()
                    write("No, the correct option is queen's crown")

    elif decision == 'no':
        write("Suspect successfully gets through the security check undetected")
        decision = suspect_weapon()  # Assign the result of suspect_weapon() to decision
        if decision == 'knife':
            move_next()
            culprit_caught_knife()
            decision = culprit_guess()
            if decision == 'bartender':
                move_next()
                write("Yes correct choice")
                move_next()
                write("The Queen sentenced the culprit to jail")
                decision = diamond_guess()
                if decision == 'crown':
                    move_next()
                    write("Yes, you guessed it correct")
                elif decision == 'saferoom':
                    move_next()
                    write("No, the correct option is queen's crown")





        # write("The party was going on very smoothly, suddenly there was a  power cut, everyone  started panicking, except Sherlock.")
        # move_next()
        # write("By taking advantage of the power cutoff, the susoect tried to sneak into the royal room to steal the royal jewel, soon as suspect tried to run from the royal room")
        # move_next()
        # write("to steal the royal diamond, soon as suspect tried to run from the royal room")
        # move_next()
        # write("The focus of the light was on the suspect in the room")
        # move_next()
        # write("Sherlock: CHECKMATE!")
        # move_next()
        # write("The lights in the palace were restored immediately, sherlock bought the culprit in front of the queen, the diamond was still in the hand of the culprit, sherlock said in")
        # move_next()
        # write("front of everyone that the diamond is fake and real diamond is safe, everyone was shocked and started murmuring and thinking about where the real diamond is.")
        # decision = culprit_guess()
        if decision == 'bartender':
            move_next()
            write("Yes correct choice")
            move_next()
            write("The Queen sentenced the culprit to jail")
            decision == diamond_guess()
            if decision == 'crown':
                write("Yes, you guessed it correct")
            elif decision == 'saferoom':
                write("No, the correct option is queen's crown")
    # elif decision == "quit":
    #     decision = quit_story()
            # Insert an image related to the treasure discovery here
    # else:
    #     write("\nLila finds her way back to the surface, encountering beautiful and mystical sights.")
    #     move_next()
            # Insert an image of Lila's return to the surface here

# elif decision == "quit":
#     decision = quit_story()

# else:
#     decision = hidden_grove()
       
#     if decision == "investigate":
#         write("\nIn the grove, Lila uncovers secrets about the forest and gains wisdom from the talking tree.")
#         move_next()
#             # Insert an image related to the talking tree here
#     elif decision == "quit":
#         decision = quit_story()
#     else:
#         write("\nLila decides to return to the forest path, ready for new adventures.")
#         move_next()
            # Insert an image of Lila on a new path here

#     elif decision == "quit":
#         conclusion()
#     decision = quit_story()

# else:
#     write("\nChoosing to stay back, Lila finds a mysterious map in her attic, hinting at future adventures.")
#     move_next()
    # Insert an image of Lila finding the map here
# conclusion()
done()