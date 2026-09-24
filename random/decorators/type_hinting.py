# type hinting number: int = 23, text: str = "hello"
# flag: bool = True, data: dict = {"key": "value"}, items: list = [1, 2, 3]
# we can also have multiple types e.g. number_or_text: int | str = 42
# and in functions we can use type hints for parameters and return types
# for example: def (num: int) -> str: return str(num)
# where -> str indicates the return type of the function is a string
# we can also use type hints for more complex data structures like lists, tuples and dictionaries
# e.g. my_list: list[int] = [1, 2, 3]. my_tuple: tuple[str, ...] = ("a", "b", "c") (... indicates that the tuple can have any number of elements of type str)
# my_dict: dict[str, str| int] = {"key1": "value1", "key2": 42} (indicates that the dictionary can have keys of type str and values of type str or int)
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b


print(add_numbers(5, 10))  # Output: 15
my_tuple: tuple[str | int | float, ...] = ("hello", 42, 3.14) # This is a tuple that can contain elements of type str, int, or float
my_dict: dict[str, str | int | float] = {"name": "Alice", "age": 30, "temperature": 98.6} # This is a dictionary that can have keys of type str and values of type str or int or float `Any` can be used to indicate that a variable can be of any type, e.g. my_var: Any = "hello" or my_var: Any = 42. However, it is generally better to use specific types whenever possible to make the code more readable and maintainable.

# to type hint a function
from typing import Callable

def decorator(func: Callable[[int, int], int]) -> Callable[[int, int], int]:
    """A decorator that takes a function with two integer parameters and returns an integer."""
    def wrapper(a: int, b: int) -> int:
        print(f"Adding {a} and {b}")
        result = func(a, b)
        print(f"Result: {result}")
        return result
    return wrapper


@decorator
def add_numbers_2(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

add_numbers_2(5, 10)  # Output: Adding 5 and 10, Result: 15