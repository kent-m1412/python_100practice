#problem77
from pathlib import Path
filepath = Path('test.txt')
print(filepath.exists())

#problem78
with open('test.txt','w') as file:
    file.write("Hello World")
