# Dictionary
quiz = {
    "Question 1": {
        "Question": "What is python?",
        "Options": ["Language", "Library", "Framework", "IDE"],
        "Answer": "Language"
    },
    "Question 2": {
        "Question": "What is the output of the following Python code? print(type(5))",
        "Options": ["int", "float", "str", "bool"],
        "Answer": "int"
    },
    "Question 3": {
        "Question": "Which of the following is used to define a function in Python?",
        "Options": ["def", "for", "if", "while"],
        "Answer": "def"
    },
    "Question 4": {
        "Question": "Which of the following methods is used to add an element to the end of a list in Python",
        "Options": ["append()", "insert()", "extend()", "remove()"],
        "Answer": "append()"
    },
    "Question 5": {
        "Question": "What will the following code output? a = 10 b = 20 print(f'a is {a} and b is {b}')",
        "Options": ["a is 10 and b is 20", "a is 20 and b is 10", "a is 10 and b is 10", "a is 20 and b is 20"],
        "Answer": "a is 10 and b is 20"
    },
    "Question 6": {
        "Question": "Which of the following will produce an error in Python?",
        "Options": ["a = 10 b = 20 print(f'a is {a} and b is {b}')", "a = 10 b = 20 print(a + b)", "a = 10 b = 20 print(a - b)", "a = 10 b = 20 print(a * b)"],
        "Answer": "a = 10 b = 20 print(a - b)"
    },
    "Question 7": {
        "Question": "What does the is keyword do in Python?",
        "Options": ["It checks if two variables point to the same object", "It checks if two variables have the same value", "It checks if two variables have the same type", "It checks if two variables have the same memory address"],
        "Answer": "It checks if two variables point to the same object"
    },
    "Question 8": {
        "Question": "Which of the following is a valid way to handle exceptions in Python?",
        "Options": ["try: ... except: ...", "try: ... finally: ...", "try: ... else: ...", "try: ... except: ... else: ..."],
        "Answer": "try: ... except: ..."
    },
}

title = "=== Quiz Game ==="
message = "Welcome to the Quiz Game related to Python 💡"

print(title)
print(message)

# initial score
score = 0

# loop through the quiz
# *50 is used to separate the question
# enumerate is used to get the index of options 
for key, value in quiz.items():
    print('\n' + '='*50)
    print(key)
    print(value["Question"])
    for i, option in enumerate(value["Options"], 1):
        print(f"{i}. {option}")

# Input loop
# .strip() is used to remove the extra spaces
    while True: 
        user_answer = input('Enter your answer (or the option number): ').strip()
        
# Check if user entered a number
# .isdigit() is used to check if the input is a number
# int() is used to convert the input to an integer
# -1 is used to convert the index to the actual option number
        if user_answer.isdigit() and 1 <= int(user_answer) <= len(value["Options"]):
            user_answer = value["Options"][int(user_answer)-1]
        
# Case-insensitive comparison
        if user_answer.lower() == value["Answer"].lower():
            print('✅ Correct! You earned a point')
            score += 1
            break
        elif user_answer.lower() in [opt.lower() for opt in value["Options"]]:
            print('❌ Incorrect. The correct answer is', value["Answer"])
            break
        else:
            print("Invalid input. Please enter a valid option or number.")

print('\n' + '='*50)
print('Quiz over! Your score is', score, '/', len(quiz), '👍')

print(f"Thankyou🌸 For playing the quiz game! 🧠")

