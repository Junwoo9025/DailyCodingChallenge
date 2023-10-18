from random import randint

easy_level = 10
hard_level = 5

#Function to check user's guess against actual answer
def check_answer(guess, answer,turns):
    """ checks ansewr against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.\nguess again.")
        return turns -1
    elif guess < answer:
        print("Too low.\nguess again.")
        return turns -1
    else:
        print(f"Congratulations!you got it right {answer} is the answer!")  
#set difficulty level    
def set_difficulty():
    level = input("choose a difficulty level: 'easy' or 'hard' ").lower()
    if level == "easy":
       return  easy_level 
    else:
        return hard_level
        




def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"the correct answer is {answer}. ")
    turns = set_difficulty()
   
   



    #Repeat the guessing functionality if they get it wrong.
    guess = 0

    #let the user guess a number and track the number of tursn reducing by 1 if you get it wrong.
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0: 
            print("you've run out of gueeses, you lose. ")
            return    


game()        