PROMPT: str = "how can I hepl you? "
JOKE: str = "Why did the electron go to therapy?Because it was feeling negative!"
SORRY: str = "Sorry I only tell jokes."

def main():
    user_input = input(PROMPT).strip()  # Get user input
    
    if user_input == "Joke" or user_input == "jokes" or user_input == "Jokes" or user_input == "joke" :  # Check if the input is exactly "Joke"
        print(JOKE)  # Print the joke
    else:
        print(SORRY)  # Print the sorry message

if __name__ == "__main__":
    main() 