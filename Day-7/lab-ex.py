# Break complex problem to Flowchart
import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choices(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for each in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
display_letter = []

while not game_over:
    guess = input("guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            display_letter.append(guess)
        elif letter in display_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        game_over = True
        print("You Lose.")

    if "_" not in display:
        game_over = True
        print("you win!") 

    print(stages[lives])
