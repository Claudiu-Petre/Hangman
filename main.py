import random

from click import clear
import hangman_words
import hangman_art
# from replit import clear 


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print(f'{guess}, you already guessed it!')

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'{guess}, is not in the word')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])