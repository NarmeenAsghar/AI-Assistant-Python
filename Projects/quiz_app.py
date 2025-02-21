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

score = 0

for key, value in quiz.items():
    print(key)
    print(value["Question"])
    for i in value["Options"]:
