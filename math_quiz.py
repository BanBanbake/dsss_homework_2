import random


def generate_random_integer(value_min, value_max):
    """
    Generate a random integer between value_min and value_max (both included).

    Args:
    value_min (int): Minimum value for the range.
    value_max (int): Maximum value for the range.

    Returns:
    int: Random integer between the specified range.
    """
    return random.randint(value_min, value_max)


def generate_operator():
    """
    Generate a random mathematical operator (+, -, *).

    Returns:
    str: Randomly chosen operator.
    """
    return random.choice(['+', '-', '*'])


def calculate_result(num1, num2, operator):
    """
    Perform the arithmetic calculation based on the given numbers and operator.

    Args:
    num1 (int): First number.
    num2 (int): Second number.
    operator (str): Mathematical operator (+, -, *).

    Returns:
    tuple: Tuple containing the problem expression and the calculated result.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer


def math_quiz():
    """
    Conducts a math quiz game with a specified number of questions.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5.5)
        operator = generate_operator()

        problem, answer = calculate_result(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
