import numbers
from typing import Callable
import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    pattern = r"\d+\.\d+|\d+"
    
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str,func: Callable):
    return sum(func(text))

total_income = sum_profit(text, generator_numbers)
print(f"Overall income is equal to {total_income}")