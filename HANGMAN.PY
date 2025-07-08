import random


words = ["apple", "tiger", "cloud", "plant", "chair"]


word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6


display_word = ["_" for _ in word]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")


while incorrect_guesses < max_incorrect and "_" in display_word:
    print("Word:", " ".join(display_word))
    guess = input("Enter a letter: ").lower()

   
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single letter.\n")
        continue
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!\n")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong! You have {max_incorrect - incorrect_guesses} tries left.\n")

if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
