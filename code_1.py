import random

comChoice = ""

comGuess = random.randint(1, 3)
if comGuess == 1:
    comChoice = "ROCK"
elif comGuess == 2:
    comChoice = "PAPER"
else:
    comChoice = "Scissor"

print(comChoice)

playerGuess = input("Type in your play: (Rock, Paper, or Scissor)")
playerChoice = playerGuess.capitalize


# def game(comChoice, playerChoice):
#     return result

# game(comGuess, guess)

