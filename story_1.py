user_name = input("Hey, What's your name? ")
print("")
print("Hi", user_name, ". Welcome to Hogwards School of Witchcraft and Wizardry!") 
print("The Sorting Ceremony will take place in a few minutes in front of the school at the Great Hall.\n")

while True:
    character_name = input("Pick a character to sort into various houses:\n 1)Harry Potter\n 2)Luna Lovegood\n 3)Draco Malfoy\n 4)Cedric Diggory: ")
    print("")
    if (character_name == "Harry Potter" or character_name == "harry potter"):
        print('Sorting Cap: "Hmm. Difficult. Very difficult. Plenty of courage, I see. Not a bad mind either. There is talent, my goodness, yes — and a nice thirst to prove yourself, now that is interesting... So where shall I put you?" \nHarry Potter: "Not Slytherin, anything but Slytherin... Please, please..." \nSorting Hat: "Not Slytherin, eh? Are you sure? You could be great, you know, it\'s all here in your head, and Slytherin will help you on the way to greatness, no doubt about that." \nHarry Potter: "Not Slytherin please..." \nSorting Hat: "No? Well, if you\'re sure — better be GRYFFINDOR!!"\n')
    elif (character_name == "Luna Lovegood" or character_name == "luna lovegood"):
        print('Sorting Cap: "This one seems an easy one. Open-minded with a dreamy disposition and a distinct flair for fashion. Transmits an aura of distinct dottiness. Honest and loyal. Very brave , and not scared to risk her own safety and even life to help her friends. I choose Ravenclaw!\n"')
    elif (character_name == "Draco Malfoy" or character_name == "draco malfoy"):
        print('Sorting Cap: "I know exactly where to put you"')
        print('Draco Malfoy: "I hate Gryffindor, I want Slytherin!"')
        print('Sorting Cap: "Slyytherinnnnn\n"')
    elif (character_name == "Cedric Diggory" or character_name == "cedric diggory"):
        print('Sorting Cap: "I think I wil put you in HUFFLEPUFF!!"\n')
    else:
        print("The charater name is not correct\n")
        continue

#     question1 = input("Do you want to proceed ahead with the next event?")
    question1 = input("Do you want to change the character? ")
    if question1 == 'No' or question1 == 'no':
        break

question2 = input("\nDo you want to proceed ahead with the next event? ")   
if(question2 == "Yes" or question2 == "yes"):
    print("\nHello ",user_name,". And welcome back to Hogwarts' first Quidditch game of the season! Today's game, Slytherin vs. Gryffindor!" )
    print("")
    print("Harry gulps and looks straight ahead as the doors open. They mount their brooms and zoom out onto the enormous pitch. There is cheering. Lee Jordan, the Quidditch commentator is announcing from a tower.")
    print("")
    story_2 = input("Select one of the conversations you would like to have:\n1)Harry and Oliver \n2)Ron and Hermoine\n")
    print("")
    harry_oliver = ["Harry and Oliver","Harry Potter","Oliver","harry and oliver","harry","oliver"]
    ron_hermione = ["Ron and Hermione","Ronald Weasley and Hermione Granger","ron and hermione","ron","hermione"]
    if (story_2 in harry_oliver):
        print('Oliver: "Scared, Harry?"\nHarry: "A little."\nOliver: "That\'s all right. I felt the same way before my first game."\nHarry: "What happened?"\nOliver: "Er, I don\'t really remember. I took a Bludger to the head two minutes in. Woke up in the hospital a week later."')
    elif (story_2 in ron_hermione):
        print("[Hermione looks through binoculars at Harry, then at Snape, who is visibly muttering]")
        print("")
        print("Hermione: It's Snape! He's jinxing the broom!\nRon: Jinxing the broom? What do we do?\nHermione: Leave it to me. \n[She hands Ron her binoculars and leaves the stands.")
        print("")
        print("[Hermione is hurrying up in the tower structures. She appears underneath Snape and touches his cloak with her wand]")
        print("Hermione: Lacarnum Inflamarae.\nA spark ignites and Snape's cloak catches fire. Hermione quickly leaves.")
        
    else:
        print("Sorry! That is not from the above list")    
else:
    print("\nGreat, Goodbye, Have a good day.")