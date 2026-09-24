# def log_call(func):
    

# def get_user(user_id):
#     ...


# def create_user(name, email):
#     ...


# def delete_user(user_id):
#     ...
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        resp = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[+]function {func.__name__} ran in {end_time - start_time:.2f} seconds")
        return resp
    return wrapper


@timer
def two_secs():
    time.sleep(2)
    print("Done")


# two_secs()


@timer
def greet(name):
    print(f"Hello {name}")


@timer
def add(a, b):
    return a + b


# greet("Tai")
# print(add(10, 20))

# result = add(10, 20)

# print(result)


def retry(num: int = 3):
    def make_retry(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                resp = func(*args, **kwargs)
                if not resp:
                    print(f"[{i+1}]Attempt for \"{func.__name__}\" fail")
                else:
                    print(f"[{i+1}]Attempt for \"{func.__name__}\" succeed")
                    return resp
        return wrapper
    return make_retry


attempts = 0


@retry(3)
def unreliable_operation():
    global attempts
    attempts += 1
    if attempts < 3:
        return not attempts < 3
    return True


print(unreliable_operation())
