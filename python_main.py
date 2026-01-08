import random

# Ensure the player enters Rock, Paper, or Scissor
def valid():
  player_choice = input("Type in your play (Rock, Paper, or Scissor): ").upper()
  while player_choice != "ROCK" and player_choice != "PAPER" and player_choice != "SCISSOR":
    print("Invalid input. Please try again.")
    player_choice = input("Type in your play (Rock, Paper, or Scissor): ").strip().upper() # .strip() removes accidental spaces
  return player_choice

# Generate the computer's choice and determine the winner
def game(player_choice):
  options = ["ROCK", "PAPER", "SCISSOR"]
  bot_choice = random.choice(options)

  if player_choice == bot_choice:
        print("It's a tie!")
  elif player_choice == "ROCK":
      if bot_choice == "PAPER":
          print("You lose!", bot_choice, "covers", player_choice)
      else:
          print("You win!", player_choice, "smashes", bot_choice)
  elif player_choice == "PAPER":
      if bot_choice == "SCISSOR":
          print("You lose!", bot_choice, "cuts", player_choice)
      else:
          print("You win!", player_choice, "covers", bot_choice)
  elif player_choice == "SCISSOR":
      if bot_choice == "ROCK":
          print("You lose!", bot_choice, "smashes", player_choice)
      else:
          print("You win!", player_choice, "cuts", bot_choice)

# Prompt the user to play again and validate Yes/No input
def ask_repeat():
  while True:
    repeat_choice = input("Would you like to play again? (Yes/No): ").strip().upper()
    if repeat_choice == 'YES' or repeat_choice == 'NO':
      return repeat_choice
    print("Invalid input. Please enter Yes or No.")

def main():
  repeat_choice = "YES"
  while repeat_choice == "YES":
      player_choice = valid()
      game(player_choice)
      repeat_choice = ask_repeat()
  print("Thank you for playing!")

main()
