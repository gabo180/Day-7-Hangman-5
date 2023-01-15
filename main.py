import random, hangman_art, hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
print("\n")
print(f'You have {lives} lives. Good Luck!')

display = []
for _ in range(word_length):
    display += "_"

#Create a empty list to store the guessed letters.
guessed_letters = []

print('===============================================')

while not end_of_game:
    while True:
        guess = input('Guess a letter: ').lower()
        if guess.isalpha():
            break
        else:
            print('\n' + 'Input should be a letter. Try again.')

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letters:
        print(f'\nYou have already guessed {guess.upper()}. Try again.\n')
        print(f"{' '.join(display)}\n")
        print('===============================================')
        continue

    #Store the letter in guessed_letters list.
    guessed_letters.append(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        # )
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(
            f'\n{guess.upper()} is not in the word.\nYou have {lives} lives remaining.'
        )
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'\nThe solution was {chosen_word.upper()}.')

    #Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
    print('===============================================')
