

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