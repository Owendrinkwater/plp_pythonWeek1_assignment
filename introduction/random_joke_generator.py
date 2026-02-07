import random

def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs 🐛",
        "Why did the Python programmer wear glasses? Because they couldn’t C 🐍",
        "I told my computer I needed a break… it said: 'No problem, I’ll go to sleep.' 😴",
        "Why was the JavaScript developer sad? Because they didn’t know how to 'null' their feelings 💔",
        "Why do Python programmers love lists? Because they don’t like being tupled 😄",
        "Debugging: Being the detective in a crime movie where you are also the criminal 🕵️‍♂️"
    ]

    joke = random.choice(jokes)
    print("\n🤣 Joke of the moment:\n")
    print(joke)

def main():
    print("🐍 Welcome to the Python Joke Generator!")

    while True:
        tell_joke()
        again = input("\nWant another joke? (yes/no): ").lower()
        if again != "yes":
            print("👋 Alright! Keep coding and keep laughing 😄")
            break

main()
