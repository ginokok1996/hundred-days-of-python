import random
import hangman_art
import hangman_words


remaining_lives = 6
chosen_word = random.choice(hangman_words.word_list)
display = []

for n in range(len(chosen_word)):
    display.append('_')

is_game_done = False
has_won = False

print(hangman_art.logo)

while is_game_done == False:
    guess = input("Guess a letter: ").lower()
    hit = False
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            hit = True
            display[index] = guess

    if hit == False:
        remaining_lives -= 1
        print(f"The letter: {guess} is not in the word")

    if remaining_lives == 0:
        is_game_done = True

    if not "_" in display:
        is_game_done = True
        has_won = True

    print(hangman_art.stages[remaining_lives])

    print(str(display))

if has_won:
    print("You have Won!")
else:
    print("You lost!")
