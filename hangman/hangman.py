import random
import hangman_words
import hangman_art
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False # Flag declaration
lives = 6

print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower() #case sensitivity

    if guess in display:
      print("You have already guessed this letter")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed wrong: {guess}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])