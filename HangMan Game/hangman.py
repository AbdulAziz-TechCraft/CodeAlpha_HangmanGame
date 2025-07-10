import random

def get_word():
    words = ["python", "hangman", "alpha", "intern", "coding"]
    return random.choice(words)

def display_progress(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = get_word()
    guessed_letters = set()
    attempts = 6

    print("🎯 Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(display_progress(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("❗ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")

        current_progress = display_progress(word, guessed_letters)
        print("Word:", current_progress)
        print("Used letters:", ', '.join(sorted(guessed_letters)))

        if '_' not in current_progress:
            print("🎉 You won! The word was:", word)
            break

    if attempts == 0:
        print("💀 You lost. The word was:", word)

# Run the game
play_hangman()
