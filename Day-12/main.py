#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)
print("Welcome to Number Guessing game")
print("I'm thinking of a number between 1 and 100")
computer_number = random.randint(1,101)
difficulty = input("Choose a difficulty. Type 'Easy' or Hard:")
attempts = 0
if difficulty == 'Hard':
  attempts = 5
elif difficulty == 'Easy':
  attempts = 10
for i in range(attempts) :
  print(f"You have {attempts} attempts remaining to guess the number")
  user_guess = int(input("Make a guess:"))
  attempts -=1
  if user_guess > computer_number:
    print("Too high")
  elif user_guess < computer_number:
    print("Too low")
  elif user_guess == computer_number:
    print(f"You got it! The answer was {computer_number}")
    break
