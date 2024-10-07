import random

# Collection of quotes
quotes = [
    "The best way to predict the future is to invent it. – Alan Kay",
    "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
    "Success is not how high you have climbed, but how you make a positive difference to the world. – Roy T. Bennett",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Do not watch the clock. Do what it does. Keep going. – Sam Levenson",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "You miss 100% of the shots you don't take. – Wayne Gretzky",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs"
]


# Function to display a random quote
def random_quote():
    return random.choice(quotes)


# Main program
def run():
    while True:
        print("\n--- Random Quote Generator ---")
        user_input = input("Press Enter to get a new quote or type 'exit' to quit: ").strip().lower()

        if user_input == 'exit':
            print("Goodbye!")
            break

        if user_input.isdigit():  # Check if input is a digit
            index = int(user_input)
            if 0 <= index < len(quotes):
                print("\n>>>", quotes[index])
            else:
                print("Please enter a valid index between 0 and", len(quotes) - 1)
        else:
            print("\n>>>", random_quote())


if __name__ == "__main__":
    run()
