import numbers
from typing import Callable


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def numbers_generator(text: str):
    return [float(numbers) for numbers in text.split() if numbers.replace('.','').isdigit()]

def sum_total(text: str,func: Callable):
    return sum(func(text))

total_income = sum_total(text, numbers_generator)
print(f"Overall income is equal to {total_income}")
