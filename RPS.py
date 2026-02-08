#RPS.py
#Name: Taran Funk
#Date: 01/03/2026
#Assignment: Lab 3 - Rock Paper Scissors
import random

def main():
  print("Let's play Rock, Paper, Scissors!")
  play = 'Y'
  wins = 0
  ties = 0
  losses = 0
  options = ['R', 'P', 'S']
  namedoptions = ['Rock', 'Paper', 'Scissors']
  while play == 'Y':

    #Get computer and user choice, both R,P,S and acual name Rock, Paper, Scissors
    compChoice = random.choice(options)
    compName = namedoptions[options.index(compChoice)]
    userChoice = input("Enter R for Rock, P for Paper, or S for Scissors: ").upper()
    userName = namedoptions[options.index(userChoice)]

    #Tie
    if userChoice == compChoice:
      print("Great minds think alike! I also chose", compName, ".")
      ties += 1

    #User wins
    elif (userChoice == 'R' and compChoice == 'S') or (userChoice == 'P' and compChoice == 'R') or (userChoice == 'S' and compChoice == 'P'):
      print("You win this time",userName, " beats ", compName, ".")
      wins += 1

    #Comp wins
    else:
      print("Ha! I got you!", compName, " beats ", userName, ".")
      losses += 1

    play = input("Would you like to play again? Enter Y for Yes, N for No: ").upper()

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
