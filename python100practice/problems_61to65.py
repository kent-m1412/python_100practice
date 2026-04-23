#problem61
def sample():
    print("Hello World")

for i in range(3):
    sample()

#problem62
def greet(name):
    print(f"Hello, {name}")

greet("Test")

#problem63
def add(a, b):
    return a + b

x = add(1,2)
print(x)

#problem64
def welcome_message(name = 'gest'):
    print(f"Hello {name} ")

welcome_message()
welcome_message('manager')

#problem65
def print_args(*args,**kwargs):
    print(args)
    print(kwargs)

print_args('A','B',key1 = "X",key2 = "Y")
