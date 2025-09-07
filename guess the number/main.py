import random
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turn=0



def check_answer(user_guess, actual_guess,turn):
    if user_guess>actual_guess:
        print("Too High")
        return turn - 1
    elif user_guess<actual_guess:
        print("Too Low")
        return turn - 1
    else:
        print("You got it! The answer was {actual_guess}")

def set_level():
    level=input("Choose a difficulty level. Type 'easy' or 'hard'")
    if level=="easy":
        global turns
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    



def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer=random.randint(1,100)
    turn=set_level()
    
    guess=0
    while guess!=answer:
        print(f"You have {turn} attemps remaining to guess the number")
        guess=int(input("make a guess:\n"))
        turn=check_answer(guess,answer,turn)
        if turn==0:
            print("You have run out of guesses! You loose.")
            return 0
game()