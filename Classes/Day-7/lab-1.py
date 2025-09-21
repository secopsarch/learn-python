# Break complex problem to Flowchart
import random
stages = ['''


''']

word_list = ['poem', 'oracle', 'space', 'economy', 'love', 'culture']

lives = 6

random.shuffle(word_list)
random_word = random.choices(word_list)
chosen_word = ''.join(random_word) 
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

#    print(stages[lives])


