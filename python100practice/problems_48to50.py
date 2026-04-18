#problem48
x = 0
try:
    print(1 / x)
except ZeroDivisionError:
    print("Division by zero")

#problem49
x = None
try:
    print(x * 2)
except TypeError as e:
    print(e)

#problem50
x = -1
if x < 0:
    raise ValueError("negative number")
