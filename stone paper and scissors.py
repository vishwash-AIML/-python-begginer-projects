import random
choices=["rock","paper","scissors"]
player=input("choose rock, paper or scissors:").lower()
computer=random.choice(choices)
if player==computer:
    print(f"it's a tie! both chose{player}.")
elif(player=="rock" and computer=="scissors") or \
(player=="paper"and computer=="rock") or \
(player=="scissors" and computer=="paper"):
 print(f" you win! {player} beats {computer}.")
else:
   print(f"computer wins!{computer} beats {player}.")