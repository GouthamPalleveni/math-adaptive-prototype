import random
def generate_puzzle(level):
    if level == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
    elif level == "Medium":
        a, b = random.randint(10, 50), random.randint(10, 50)
    else:
        a, b = random.randint(50, 100), random.randint(50, 100)

    operator = random.choice(["+", "-", "*"])
    question = f"{a} {operator} {b}"
    answer = eval(question)
    return question, answer
