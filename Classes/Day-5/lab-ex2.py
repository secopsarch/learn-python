# These exercises will help practice:

# Working with lists
# Using random selections
# Taking user input
# String manipulation
# For loops
# List methods (append, join)

# Card Dealer Generator Create a program that asks the user:
# -> How many players are playing (2-6)
# -> How many cards each player should receive (1-5) Then generate and display a random hand of cards for each player from a standard 52-card deck, without repeating cards.

import random

number_of_players = ['2', '3', '4', '5', '6', '7', '8', '9', '10']

deck_of_cards = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52']

cards_per_player = ['1', '2', '3']

players = int(input("Enter the number of players? between 2-10: \n"))
cards = int(input("How many cards each player should recieve? between 1-3: \n"))

for p in players:
    cards_list = random.choice(players * cards)

random.shuffle(deck_of_cards)
cards_each = ''.join(deck_of_cards)
print(f"number of cards per player: {cards_each}")
#deck = 

# for n in a:
#     cards.append(random.choice(cards_per_player))
# print(f"the total cards per player is: {cards}")

    







# Custom Username Generator Write a program that helps create usernames by asking the user:
# How many letters they want from their first name
# How many letters they want from their last name
# How many random numbers to add
# If they want special characters (y/n) Then generate 3 different username options based on their input.
