import random
from hangman_word import word_list
from hangman_art import logo
stages = [
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """
]
print(logo)
chosen_word = random.choice(word_list)
# Create placeholders
word_length = len(chosen_word)
display = "_" * word_length
print(display)

lives = 6
game_over = False
correct_letters = []

while not game_over:
    print(f"*******************{lives}/6 Lives left*******************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue

    new_display = ""
    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} that isn't in the word. You lose a life.")
        print(stages[6 - lives])  # show hangman stage
        if lives == 0:
            game_over = True
            print("*******************Game Over! You lose.***************")

    if "_" not in display:
        game_over = True
        print("*******************You win!***************")
