#Step 5

import random, hangman_art, hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
print("\n")
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
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

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letters:
        print(f'\nYou have already guessed {guess.upper()} \n')
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
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'{guess.upper()} is not in the word.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
    print('===============================================')
