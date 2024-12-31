############### Blackjack Project #####################
import art
import random
import os

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def play_game():
  print(art.logo)
  def deal_card():
    deal_card = random.choice(cards)
    return deal_card
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)
  while not game_over:
    user_score = calc_score(user_cards)
    comp_score = calc_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or comp_score == 0 or user_score > 21:
      game_over = True
    else:
      to_cont = input("Type 'y' to get another card or 'n' to pass:")
      if to_cont == "y":
        user_cards.append(deal_card())
      else:
        game_over = True
  
  while comp_score != 0 and comp_score < 17:
    computer_cards.append(deal_card())
    comp_score = calc_score(computer_cards)
  def compare(user_score, comp_score):
    if user_score == comp_score:
      return "Draw😒"
    elif comp_score == 0:
      return "Lose, opponent has Blackjack😵"
    elif user_score == 0:
      return "Win with a Blackjack😍"
    elif user_score > 21:
      return "You lose.😵"
    elif comp_score > 21:
      return "You win.😍"
    elif user_score > comp_score:
      return "You win.😍"
    else:
      return "You lose.😵"
  print(compare(user_score, comp_score))
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {comp_score}")

while input("Do you want to play Blackjack: 'Y' or 'N' :") == "Y":
  os.system('clear')
  play_game()