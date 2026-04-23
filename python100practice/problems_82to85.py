#problem82
import csv
lst = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

with open("test.csv",'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(lst)

#problem83
with open("test.csv","r",newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

lst = [
    {"id":"0001","name":"admin"},
    {"id":"0002","name":"guest"},
    {"id":"0003","name":"test"},
]

#problem84
with open("test.csv","w",newline ='') as file:
    writer = csv.DictWriter(file,fieldnames=['id','name'])
    writer.writeheader()
    writer.writerows(lst)

#problem85
with open("test.csv","r",newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
