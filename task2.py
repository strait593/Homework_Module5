import numbers
from typing import Callable

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    return [float(numbers) for numbers in text.split() if numbers.replace('.','').isdigit()]

def sum_profit(text: str,func: Callable):
    return sum(func(text))

total_income = sum_profit(text, generator_numbers)
print(f"Overall income is equal to {total_income}")