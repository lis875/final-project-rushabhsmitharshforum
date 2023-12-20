from turtle import *
import turtle
import turtle
style1 = ('Arial', 13)

def move_next():
    penup()
    right(90)
    forward(18)
    left(90)
    pendown()

def resultt():
    move_next()
    write("The focus of the light was on the suspect in the room", font=style1)
    move_next()
    write("Sherlock: CHECKMATE!", font=style1)
    move_next()
# def passcode():
#     write("Suspect is trying to enter the Passcode", font=style1)
    
#     return make_choice("Enter the Independance Day of America", ["1947", "1947"])
def passcode():
    write("Suspect is trying to enter the Passcode", font=style1)    
    passcode_input = textinput("Input","Enter the Independance Day of America")
    if(passcode_input == "1776"):
        move_next()
        write("Jewel is stolen", font=style1)    
        resultt()
    else:
        move_next()
        write("Intruder Alert! The siren goes on", font=style1)    
        resultt()

passcode()
done()


