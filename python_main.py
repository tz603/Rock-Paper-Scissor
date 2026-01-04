import random

while True:
  bot_choice = ""
  bot_choice = random.randint(1, 3)
  if bot_choice == 1:
      bot_choice = "ROCK"
  elif bot_choice == 2:
      bot_choice = "PAPER"
  else:
      bot_choice = "SCISSOR"

  player_guess = input("Type in your play (Rock, Paper, or Scissor): ")
  player_choice = player_guess.upper()

  if player_choice == bot_choice:
    print("It's a tie!")

  if player_choice == "ROCK":
      if bot_choice == "PAPER":
          print("You lose!", bot_choice, "covers", player_choice)
      else:
          print("You win!", player_choice, "smashes", bot_choice)

  if player_choice == "PAPER":
      if bot_choice == "SCISSOR":
          print("You lose!", bot_choice, "cuts", player_choice)
      else:
          print("You win!", player_choice, "covers", bot_choice)
    
  if player_choice == "SCISSOR":
      if bot_choice == "ROCK":
          print("You lose!", bot_choice, "smashes", player_choice)
      else:
          print("You win!", player_choice, "cuts", bot_choice)
  repeat_entered = input("Would you like to play again? (Yes/No): ")
  repeat_choice = repeat_entered.upper()
  if repeat_choice == 'NO':
    break
