import random

# List of words to guess
words = ["python", "programming", "hangman", "computer", "keyboard", 
         "developer", "function", "variable", "loop", "string"]

def choose_word():
    return random.choice(words)

def display_board(wrong_guesses, word_display, guessed_letters):
    # Hangman stages (0 to 6 wrong guesses)
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ==========""",
    ]

    print(stages[wrong_guesses])
    print(f"\nWord: {' '.join(word_display)}")
    print(f"Wrong guesses left: {6 - wrong_guesses}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

def get_guess(guessed_letters):
    while True:
        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter!")
        else:
            return guess

def play_hangman():
    print("Welcome to Hangman!")
    print("You have 6 wrong guesses before the man is hanged.\n")

    word = choose_word()                       
    word_display = ["_"] * len(word)           
    guessed_letters = set()                 
    wrong_guesses = 0                           

    while wrong_guesses < 6 and "_" in word_display:
        display_board(wrong_guesses, word_display, guessed_letters)

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"✓ '{guess}' is in the word!")
            # Reveal all positions of the guessed letter
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            print(f"✗ '{guess}' is NOT in the word!")
            wrong_guesses += 1

    # Game over - check result
    display_board(wrong_guesses, word_display, guessed_letters)

    if "_" not in word_display:
        print(f"\n You won! The word was '{word}'!")
    else:
        print(f"\n You lost! The word was '{word}'.")

    return input("\nPlay again? (y/n): ").lower() == "y"

# Main loop
while play_hangman():
    print("\n--- New Game ---\n")

print("\nThanks for playing!")
import random

# List of words to guess
words = ["python", "programming", "hangman", "computer", "keyboard", 
         "developer", "function", "variable", "loop", "string"]

def choose_word():
    return random.choice(words)

def display_board(wrong_guesses, word_display, guessed_letters):
    # Hangman stages (0 to 6 wrong guesses)
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ==========""",
    ]

    print(stages[wrong_guesses])
    print(f"\nWord: {' '.join(word_display)}")
    print(f"Wrong guesses left: {6 - wrong_guesses}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

def get_guess(guessed_letters):
    while True:
        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter!")
        else:
            return guess

def play_hangman():
    print("Welcome to Hangman!")
    print("You have 6 wrong guesses before the man is hanged.\n")

    word = choose_word()                       
    word_display = ["_"] * len(word)           
    guessed_letters = set()                 
    wrong_guesses = 0                           

    while wrong_guesses < 6 and "_" in word_display:
        display_board(wrong_guesses, word_display, guessed_letters)

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"✓ '{guess}' is in the word!")
            # Reveal all positions of the guessed letter
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            print(f"✗ '{guess}' is NOT in the word!")
            wrong_guesses += 1

    # Game over - check result
    display_board(wrong_guesses, word_display, guessed_letters)

    if "_" not in word_display:
        print(f"\n You won! The word was '{word}'!")
    else:
        print(f"\n You lost! The word was '{word}'.")

    return input("\nPlay again? (y/n): ").lower() == "y"

# Main loop
while play_hangman():
    print("\n--- New Game ---\n")

print("\nThanks for playing!")