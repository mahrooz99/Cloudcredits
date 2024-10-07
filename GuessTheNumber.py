import random


class GuessTheNumberGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 10
        self.score = 0
        self.difficulty = None

    def display_intro(self):
        print("Welcome to Guess the Number!")
        print("I have selected a number between 1 and 100.")
        print(f"You have {self.attempts} attempts to guess the number.")

    def set_difficulty(self):
        while True:
            print("\nChoose your difficulty level:")
            print("1. Easy (10 attempts)")
            print("2. Medium (7 attempts)")
            print("3. Hard (5 attempts)")
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                self.attempts = 10
                self.difficulty = "Easy"
                break
            elif choice == '2':
                self.attempts = 7
                self.difficulty = "Medium"
                break
            elif choice == '3':
                self.attempts = 5
                self.difficulty = "Hard"
                break
            else:
                print("Invalid choice. Please select a valid difficulty level.")

    def get_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if 1 <= guess <= 100:
                    return guess
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def check_guess(self, guess):
        if guess == self.secret_number:
            self.score += 10 * self.attempts  # Scoring system: points based on remaining attempts
            return True
        elif guess < self.secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        return False

    def provide_hint(self):
        if self.secret_number % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")

        if self.secret_number > 50:
            print("Hint: The number is greater than 50.")
        else:
            print("Hint: The number is 50 or less.")

    def play(self):
        self.set_difficulty()
        self.display_intro()

        while self.attempts > 0:
            guess = self.get_guess()
            if self.check_guess(guess):
                print(f"Congratulations! You guessed the number {self.secret_number} correctly.")
                break

            self.attempts -= 1
            print(f"Remaining attempts: {self.attempts}")

            if self.attempts <= 3:  # Provide a hint when attempts are low
                self.provide_hint()

        if self.attempts == 0:
            print(f"Sorry, you've run out of attempts. The number was {self.secret_number}.")

        print(f"Your final score: {self.score}")


def main():
    while True:
        game = GuessTheNumberGame()
        game.play()

        replay = input("Would you like to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
