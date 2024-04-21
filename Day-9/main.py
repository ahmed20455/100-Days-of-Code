from replit import clear

from art import logo

print(logo)
#HINT: You can call clear() to clear the output in the console.
bidders = {}
set_choice = "True"
while set_choice == "True":
  name = input("What is your name ?")
  bid = input("What is your bid ? $")
  bidders[name] = bid
  choice = input("Are there any other bidders ? Type 'yes' or 'no'")
  if choice == "yes":
    clear()
  elif choice == "no":
    set_choice = "False"
for key in bidders:
  max_bid = 0
  if int(bidders[key]) > max_bid:
    max_bid = bidders[key]
    winner = key
    print(f"Winner is {winner} with a bid of $ {max_bid}")
