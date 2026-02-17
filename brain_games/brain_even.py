import numbers
import prompt
from random import randint


def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


def greeting():
    print('Welcome to the Brain Games!')


def even():
    greeting()
    name = prompt.string('May I have your name? ')
    print(
        f"Hello, {name}!"
        f'\nAnswer "yes" if the number is even, otherwise answer "no".')
    
    item = 0
    while item < 3:
        number = randint(1, 100)
        question, correct_answer = f'Question: {str(number)}', 'yes' if is_even(number) else 'no'
        print(f'{question}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
            item += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!")
            break
        if item == 3:
            print(f"Congratulations, {name}!")
