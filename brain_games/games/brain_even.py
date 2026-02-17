from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


def generate_data() -> str:
        number = randint(1, 100)
        question, correct_answer = f'{str(number)}', 'yes' if is_even(number) else 'no'
        return question, correct_answer
