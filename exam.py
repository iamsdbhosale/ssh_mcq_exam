import json
import os

def load_questions():
    with open("questions2.json", "r") as f:
        return json.load(f)

def run_exam(username):
    questions = load_questions()
    score = 0
    answers = []

    print(f"\nWelcome {username}, starting your exam...\n")

    for q in questions:
        print(f"Q{q['id']}: {q['question']}")
        for opt in q['options']:
            print(opt)            
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        answers.append({'id': q['id'], 'your_answer': ans})
        print("--------------------------------------------")
        #os.system('cls' if os.name == 'nt' else 'clear') // it helps to clear the screen
        if ans == q['answer']:
            score += 1

    print(f"\nExam Completed! Your Score: {score}/{len(questions)}")
    print("--------------------------------------------")
    print("Thank You!!!")
    os.makedirs("results", exist_ok=True)
    with open(f"results/{username}.json", "w") as f:
        json.dump({"username": username, "score": score, "answers": answers}, f, indent=2)

if __name__ == "__main__":
    username = input("Enter your name: ")
    run_exam(username)
