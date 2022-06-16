"""
Name(s): Silas Smith, Jacob Baglione
Name of Project: Rock Paper Scissors Best of Three
"""

import random
options=['Rock','Paper','Scissors']
name=input("Enter your name: ")
ComputerScore=0 
PlayerScore=0
NumberOfRounds=0
gameOn=True
print(f"Welcome {name.title()}")
while NumberOfRounds<3:
  ComputerOption=random.choice(options)
  PlayerOption=input("Enter Rock/ Paper/ Scissors: ").title()
  print(f"Computer option: {ComputerOption}")
  print(f"{name.title()} option: {PlayerOption}")
  NumberOfRounds += 1
  if ComputerOption==PlayerOption:
    print('Tie')
  elif (ComputerOption=='Rock' and PlayerOption == 'Scissors') or (ComputerOption=='Scissors' and PlayerOption=='Paper') or (ComputerOption=='Paper' and PlayerOption=='Rock'):
    print("Computer wins")
    ComputerScore += 1
  elif (PlayerOption=='Rock' and ComputerOption == 'Scissors') or (PlayerOption=='Scissors' and ComputerOption=='Paper') or (PlayerOption=='Paper' and ComputerOption=='Rock'):
    print(f"{name.title()} wins")
    PlayerScore += 1
  else:
    print("Trolololol noone wins.") 
#its not a bug its a feature LOL
  print("-------------------------")
  print("")
  print(f"Round No: {NumberOfRounds}")
  print("------ Score Board ------")
  print(f"{name.title()}: {PlayerScore} | Computer: {ComputerScore}")
  print("===============================")
  print("")
  if NumberOfRounds==3:
    if PlayerScore==ComputerScore:
      print("Game over.  Its a draw!!")
    elif PlayerScore>ComputerScore:
      print(f"Congrats {name.title()}, You won the game!!")
    else:
      print(f"L Bozo you lose. The computer won the game!! Better luck next time {name.title()}!")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "y":
      NumberOfRounds = 0
    else:
      break