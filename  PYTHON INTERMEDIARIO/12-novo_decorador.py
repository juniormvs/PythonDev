from decorator import my_decorator, uppercase_decorator, split_string

@my_decorator
def my_function():
    print("Dentro da função")

my_function()

@split_string
@uppercase_decorator
def text():
    return "Hello world"

print(text())

@split_string
@uppercase_decorator
def example():
    return "Criando exemplos e utilizando decorator"


print(example())
