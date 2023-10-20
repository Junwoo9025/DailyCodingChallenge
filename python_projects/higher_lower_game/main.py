from art import logo,vs
from game_data import data
import random


def format_data(account):
  #docstrings = input and output to clearify
  """Takes the account data and return the printable format."""
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return (f"{account_name}, a {account_description} from {account_country}")



def check_answer(guess, a_followers, b_followers):
  '''take the user guess and follower counts and returns if they got it right'''
  if a_followers > b_followers:
      return guess == "a"
  else:
     return guess == "b"

#Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

#Make the game repeatable.
while game_should_continue == True:

  #Generate a random account from the game data.

    #Making account at position B become the next account at postion A.
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)

  print(f"compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  #Ask user for a guess.
  guess = input("who has more follower? Type 'A' or 'B': ").lower()

  #Check if user is correct.
  #Get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess ,a_follower_count, b_follower_count)

  #Give user feedback on their guess.
  #Score keeping.
  if is_correct:
    score += 1
    print(f"You are right! Current socre: {score}.")
  else:
    game_should_continue = False
    print(f"you are wrong! Finally score: {score}.")   





