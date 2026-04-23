#problem91
from python100practice.problems_51to60 import char

x = []
with open("output.txt","w",newline="") as file:
    for i in range(10):
        for j in range(10):
            number = str(i*j)
            if "3" in number:
                file.write(f"{i} * {j} = {number}\n")

#problem92
def find_numbers(start, end):
    target_range = range(start, end)
    return {num for num in target_range if "3" in str(num)}

#problem93
x = str(input("Enter 1-digit integer"))
count = 0
num = 1
y = []
while count < 10:
    if x in str(num):
        y.append(num)
        count += 1
    num += 1
for i in y:
    print(i)

#problem94
data = [
    ('001', '001', {1, 4}),
    ('001', '002', {2, 7, 8, 9}),
    ('001', '003', {2, 3}),
    ('001', '004', {5}),
    ('001', '005', {6, 7, 8}),
    ('002', '001', {3, 7}),
    ('002', '002', {9}),
    ('002', '003', {3, 8}),
    ('002', '004', {2}),
    ('002', '005', {3, 5}),
]

for x,y,z in data:
    if len(z) == 1:
        print(x,y,z)

#problem95
target_text = "Python is a programming language that lets you work quickly and integrate systems more effectively"
words = target_text.split()
for word in words:
    if len(word) <= 4:
        print(word)

#problem96
def reverse_dict(dictionary):
    try:
        output = {x:y for y,x in dictionary.items()}
    except Exception:
        return None
    return output

#problem97
with open("test.txt", "r",newline = '') as file:
    data = file.read()
    count = {}
    for char in data:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for key,value in count.items():
        print(f"{key}: {value}")

#problem98
class StringJoiner:
    def __init__(self):
        self.items = []
    def append(self,item):
        if item is not None:
            self.items.append(str(item))
    def join(self,delimiter = ""):
        return delimiter.join(self.items)

target_list = [1,2,3,None,5,None,7]
sj = StringJoiner()
for item in target_list:
    sj.append(item)
result = sj.join("&")
print(result)

#problem99
from pprint import pprint
lst = [1,2,3,None,5,None,7]
converted_list = []
source = []
for item in lst:
    if item is None:
        continue
    if item % 2 == 0:
        continue
    new_item = 2 * item
    converted_list.append(new_item)
    source.append({"index":new_item,"from":item,"to":new_item})

pprint(source)

#problem100
import csv
filepath = 'input.csv'

with open(filepath, 'r', newline='') as file:
    reader = csv.DictReader(file)
    data_list = list(reader)

data_set = {
    data_dict['user_id']
    for data_dict in data_list
    if data_dict['operation'] == 'OP02_010'
}

for user_id in data_set:
    print(user_id)
