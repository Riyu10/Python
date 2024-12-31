import os
import art

print(art.logo)
bidders = {}
def add_bidder(name, bid):
  bidders[name] = bid
def highest_bid(bidders):
  highest_bid = 0
  for bidder in bidders:
    if bidders[bidder] > highest_bid:
      highest_bid = bidders[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
more_bidders = True
while more_bidders:
  name = input("What is your name?:\n")
  bid = int(input("What is your bid?:\n"))
  add_bidder(name, bid)
  more_bid = input("Are there any other bidders? 'Yes' or 'No'\n")
  if more_bid == "No":
    more_bidders = False
    highest_bid(bidders)
  else:
    os.system('clear')