

####### Decorators #######
#  for a simple decorator:
def fence(func):
    def wrapper():
        print("+" * 10)
        func()
        print("+" * 10)
    return wrapper


@fence
def say_a_word():
    print("werd is a word")


say_a_word()


# for a decorator with parameters:
def custom_fence(char: str = "+"):
    def add_fence(func):
        def wrapper():
            print(char * 10)
            func()
            print(char * 10)
        return wrapper
    return add_fence

@custom_fence(char="*")
def say_a_word():
    print("werd is a word")

say_a_word()


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
