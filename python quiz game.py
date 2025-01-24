import random

def ask_Question(question, choices, answer, score_value):
    print(question)

    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    
    user_answer = input("Enter the number of your choice: ")

    if choices[int(user_answer)-1].lower() == answer.lower():
        print("Correct!")
        return score_value
    else:
        print(f"Wrong! The correct answer is: {answer}")
        return 0


def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["Paris", "London", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        
        {
        "question":"what is the capial of japan?",
        "choices": ["Seoul", "beijing", "Tokyo", "Bangkok"],
        "answer": "Tokyo"
        },
        
        {
        "question":"what is 216+1050?",
        "choices": ["1266", "127", "1288", "1366"],
        "answer": "1266"
        },
        {
        "question":"what is the largest planet in our solar system?",
        "choices":["mars","jupiter","saturn","earth"],
        "answer": "jupiter"
        },
        
        {
        "question":"what year did the ttanic sink?",
        "choices":["1905","1912","1918","9215"],
        "answer": "1912"    
        },
        
        {
        "question":"what is the boiling oint of water in celsius?",
        "choices":["90","9","100","105"],
        "answer": "100"
        },
        
        {
         "question":"who painted the mona lisa?",
        "choices":["vincen van gogh ","pablo picasso","claude monet","leonardo da vinci"],
        "answer": "leonardo da vinci"
        },
        
        {
         "question":"what i the square root of 64?",
        "choices":["6","7","8","9"],
        "answer": "8"
        },
        
        {
        "question":"what is the chemical symbol for gold? ",
        "choices":["Ag","Au","Pb","Pt"],
        "answer": "Au"
        },
        
        {
            "question":"how many minutes are in a full week?",
        "choices":["10090","10181","1099","10080"],
        "answer": "10080"
        }
    ]
    
    total_score = 0
  
    for q in questions:
        score = ask_Question(q["question"], q["choices"], q["answer"], 10)
        total_score += score
        
    print(f"Your final score is {total_score}/100")


if __name__ == "__main__":
    main()
