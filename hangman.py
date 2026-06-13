import random

# List of words
words = ["python", "computer", "programming", "hangman", "student"]

# Randomly select a word
word = random.choice(words)

# Hangman stages
stages = [
"""
-----
|   |
|
|
|
|
=========
""",
"""
-----
|   |
|   0
|
|
|
=========
""",
"""
-----
|   |
|   0
|  /|
|
|
=========
""",
"""
-----
|   |
|   0
|  /|\
|
|
=========
""",
"""
-----
|   |
|   0
|  /|\
|   |
|
=========
""",
"""
-----
|   |
|   0
|  /|\
|   |
|  /
|  
=========
""",
"""
-----
|   |
|   0
|  /|\
|   |
|  / \
|
=========
"""
]

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("===== HANGMAN GAME =====")

while wrong_guesses < max_attempts:
    
    # Display hangman structure
    print(stages[wrong_guesses])

    # Display hidden word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess! Attempts left:", max_attempts - wrong_guesses)

# Game Over
if wrong_guesses == max_attempts:
    print(stages[6])
    print("\nGame Over!")
    print("The word was:", word)