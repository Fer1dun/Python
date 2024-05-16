from pickle import NONE
import random
from secrets import choice
choices=["rock","paper","scissors"]
computer=random.choice(choices)
player=None
while player not in choices:
    player=input("choice rock or paper or scissors\n").lower()
print("computer:"+computer,"\nplayer:"+player)
if computer=="rock":
    if player=="rock":
        print("draw")
    elif player=="paper":
        print("player won")
    elif player=="scissors":
        print("computer won")
elif computer=="paper":
    if player=="paper":
        print("draw")
    elif player=="scissors":
        print("player won")
    elif player=="rock":
        print("computer won")
elif computer=="scissors":
    if player=="scissors":
        print("draw")
    elif player=="rock":
        print("player won")
    elif player=="paper":
        print("computer won")

