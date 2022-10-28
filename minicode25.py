#!/usr/bin/env python3
'''Brendan's mini project. Rock, Paper, Scissors'''
import random

def main():
 while True:
    print("Welcome to a game of Rock, Paper, Scissors")
    options = ["Rock", "Paper", "Scissors"]
    comp_cho = random.choice(options)
    print("Your turn to play")
    user_sel = input("Rock, Paper, or Scissors?  ")
    print(f"You chose {user_sel}, computer chose {comp_cho}.") 
    if comp_cho==user_sel:
        print("You tied")
    elif comp_cho=="Rock" and user_sel=="Paper":
        print("Paper covers rock, You win")
    elif comp_cho=="Paper" and user_sel=="Rock":
        print("Paper covers rock, You loose!")
    elif comp_cho=="Scissors" and user_sel=="Paper":
        print("Scissors cut paper, You loose!")
    elif comp_cho=="Paper" and user_sel=="Scissors":
        print("You win!")
    elif comp_cho=="Rock" and user_sel=="Scissors":
        print("You loose!")
    elif comp_cho=="Scissors" and user_sel=="Rock":
        print("You win!")
    else:
        print("Sorry, try again and choose only from the choices provided")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
main()
