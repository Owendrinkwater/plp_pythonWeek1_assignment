def run_quiz():
    questions = [
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["A. func", "B. define", "C. def", "D. function"],
            "answer": "C"
        },
        {
            "question": "Which movie features the character 'Neo'?",
            "options": ["A. Inception", "B. The Matrix", "C. Avatar", "D. Interstellar"],
            "answer": "B"
        },
        {
            "question": "What does HTML stand for?",
            "options": [
                "A. HyperText Markup Language",
                "B. HighText Machine Language",
                "C. HyperTool Markup Language",
                "D. Home Tool Markup Language"
            ],
            "answer": "A"
        }
    ]

    score = 0

    print("\n🎮 Welcome to the Quiz Game!\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print(f"🏁 Quiz finished! Your score: {score}/{len(questions)}")

def main():
    while True:
        run_quiz()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("👋 Thanks for playing! See you next time.")
            break

main()
