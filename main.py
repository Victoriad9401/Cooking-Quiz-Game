import random
import time

def quiz_game():
    print("Welcome to the Cooking Quiz!!")
    print("Test the knowledge of cooking recipies.")
    print("Type the correct option (A,B,C, or D in caps for your answer.\n")


    questions = [
        {
            "question": "What is the process of cooking food in small amount of oil over medium-high heat called?",
            "options": ["A. Boiling", "B. Frying", "C. Sauteing", "D. Grilling"],
            "answer": "C"
        },
        {
            "question": "Which spice is known as 'the queen of spices'?",
            "options": ["A. Cardamom", "B. Cinnamon", "C. Nutmeg", "D. Clove"],
            "answer": "A"
        },
        {
            "question": "True or False: Baking sode & Baking powered are the same",
            "options": ["A. True", "B. False"],
            "answer": "B"
        },
        {
            "question": "To make a roux, you need equal parts of _ and flour.",
            "options": ["A. Batter", "B. Baking powder", "C. Water ", "D. Butter"],
            "answer": "D"
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["A. Avocado", "B. Lime", "C. Tomatoes ", "D. Cilantro"],
            "answer": "A"
        }
    ]

    random.shuffle(questions)
    score = 0

    for idx, q in enumerate(questions):
        print(f"Question {idx + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your Answer: ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {q['answer']}.\n")
        time.sleep(1)
    print(f"Quiz is Over! your final Score is {score}/{len(questions)}.")

if __name__ == "__main__":
    quiz_game()
