import random
from hangmanwords import word_list
from hangman_acii import stage

lives=6

choosen_word=random.choice(word_list)
print(choosen_word)


placeholder=""
word_length=len(choosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder) 

game_over=False
correct_letters=[]


while not game_over:
    guess=input("guess the letter").lower()

    if guess in correct_letters:
        print(f"you have already guessed {guess}")
    disp=""
    for letter in choosen_word:
        if letter==guess:
            disp+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            disp+=letter
        else:
            disp+="_"

    print(disp)
    

    if guess not in choosen_word:
        lives-=1
        print("you guessed wrong, you lose a life")
        if lives==0:
            game_over=True
            print("you loose")

    if "_" not in disp:
        game_over=True
        print("you win")


    print(stage[lives])


