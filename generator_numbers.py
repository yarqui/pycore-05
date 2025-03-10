from typing import Callable, Generator
import re


def generator_numbers(text: str) -> Generator:
    number_regex = r" \d+\.\d+ | \d+ "  # matches both floats & integers

    for match in re.finditer(number_regex, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))


text = "The employee's total income consists of several parts: 1000.01 as the main income, supplemented by additional income of 27.45 and 324.00 dollars"
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
