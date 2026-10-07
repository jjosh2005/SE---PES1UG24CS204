import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    def __init__(self, length=None):
        self.length = length
        self.target = None
        self.history = []

    def choose_length(self):
        while True:
            choice = input("Choose word length (4, 5, or 6): ").strip()

            if choice in {"4", "5", "6"}:
                self.length = int(choice)
                return

            print("Please choose 4, 5, or 6.")

    def display_history(self):
        print("\nGuess history:")
        for guess, feedback in self.history:
            print(f"  {guess}: {' '.join(feedback)}")

    def session_summary(self, outcome):
        print("\nSession summary:")
        print(f"Result: {outcome}")
        print(f"Word length: {self.length}")
        print(f"Accepted guesses: {len(self.history)}/6")
        print(f"Target word: {self.target}")
        self.display_history()

    def run(self):
        # Select the mode before choosing the target word.
        if self.length is None:
            self.choose_length()
        elif self.length not in {4, 5, 6}:
            raise ValueError("Word length must be 4, 5, or 6.")

        candidates = [word for word in WORDS if len(word) == self.length]

        if not candidates:
            print(f"No {self.length}-letter words are available.")
            return

        self.target = random.choice(candidates)
        self.history = []

        print(f"Wordle ({self.length} letters, 6 guesses.)")

        while len(self.history) < 6:
            guess = input("> ").strip().lower()

            if guess == "q":
                print("Game quit.")
                self.session_summary("Quit")
                return

            # Invalid guesses do not consume a turn or enter the history.
            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue

            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            print(" ".join(feedback))
            self.display_history()

            if guess == self.target:
                print(f"Solved in {len(self.history)} guesses!")
                self.session_summary("Won")
                return

        print(f"Out of guesses. The word was: {self.target}")
        self.session_summary("Lost")
