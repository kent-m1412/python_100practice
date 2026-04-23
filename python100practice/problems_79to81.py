#problem79
with open('test.txt','a') as file:
    file.write("\nHello World")

#problem80
with open('test.txt','r') as file:
    content = file.read()
    print(content)

#problem81
from pathlib import Path

file = Path('test.txt')
if file.exists():
    file.unlink()
else:
    print('file does not exist')
