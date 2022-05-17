#Hang Man

import sys
import random
import turtle

screen = turtle.Screen()
screen.setup(500,500)

arm_length = 100
leg_length = 120
my_turtle = turtle.Turtle()
def reset():
  my_turtle.pu()
  my_turtle.setpos(0,0)
  my_turtle.pd()

reset()

def draw_head():
  my_turtle.seth(90) 
  my_turtle.fd(30)
  my_turtle.rt(90)
  my_turtle.circle(50)
  reset()

def draw_torso():
  my_turtle.right(90)
  my_turtle.pd()
  my_turtle.forward(50)
  reset()

def draw_left_arm():
  my_turtle.seth(160)
  my_turtle.fd(arm_length/2)
  my_turtle.rt(20)
  my_turtle.fd(arm_length/2)
  reset()

def draw_right_arm():
  my_turtle.seth(20)
  my_turtle.fd(arm_length/2)
  my_turtle.lt(20)
  my_turtle.fd(arm_length/2)
  reset()

def draw_left_leg():
  my_turtle.seth(270)
  my_turtle.fd(50)
  my_turtle.seth(230)
  my_turtle.fd(leg_length/2)
  my_turtle.lt(40)
  my_turtle.fd(leg_length/2)
  reset()

def draw_right_leg():
  my_turtle.seth(270)
  my_turtle.fd(50)
  my_turtle.seth(310)
  my_turtle.fd(leg_length/2)
  my_turtle.rt(40)
  my_turtle.fd(leg_length/2)

def convert(Word):
    new = ""
    for x in Word:
        new += x 
    return new

Guesses = 6

with open('C:\\Users\\tulda\\Desktop\\TEXT FILES\\RANDOM WORD LIST.txt') as f:
    RandomWord = f.read()
    Text = list(map(str, RandomWord.split()))
    OtherWord = random.choice(Text)

PlaceHolder = '*' * len(OtherWord)
while '*' in PlaceHolder:
    print(PlaceHolder)
    OW = (str(input("Guess a Letter: \n"))).lower()
    if(OW in OtherWord):
        print("Correct")
        Templist = [pos for pos, char in enumerate(OtherWord) if char == OW]
        for x in Templist:
            PlaceHolder = PlaceHolder[:x] + OW + PlaceHolder[x + 1:]
    else:
        print("Incorrect")
        Guesses -= 1
        print(f"Incorrect Guesses Left: {Guesses}")
        if (Guesses == 5):
          draw_head()
        elif(Guesses == 4):
          draw_torso()
        elif(Guesses == 3):
          draw_left_arm()
        elif(Guesses == 2):
          draw_right_arm()
        elif(Guesses == 1):    
          draw_left_leg() 
        elif(Guesses == 0):
          draw_right_leg()
          print("YOU LOSE!!!")
          sys.exit()

print(PlaceHolder)
print("YOU WIN!!!")
sys.exit()