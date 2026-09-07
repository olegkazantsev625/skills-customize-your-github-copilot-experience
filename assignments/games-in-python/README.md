
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python. Practice string manipulation, loops, conditionals, lists, user input, and random selection while creating a game where players guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Build the Game Setup

#### Description

Complete the setup for the game by selecting a secret word from the provided list and creating the variables needed to track the player's progress.

#### Requirements

Completed program should:

- Randomly select one word from the predefined `words` list.
- Store the player's guessed letters.
- Track the number of incorrect guesses.
- Set a maximum number of incorrect guesses allowed.

### 🛠️ Implement the Guessing Game

#### Description

Complete the main game loop so the player can guess letters, see their progress, and receive a final result when the word is guessed or the attempts are exhausted.

#### Requirements

Completed program should:

- Display the current progress using underscores for letters that have not been guessed, such as `_ _ _ _`.
- Ask the player to enter a letter and update the game state after each guess.
- Track incorrect guesses and stop the game when the maximum is reached.
- End when the player guesses every letter in the secret word or runs out of attempts.
- Display a clear win message or reveal the secret word in a lose message.
