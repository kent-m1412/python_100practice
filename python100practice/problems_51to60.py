#problem51
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}")

#problem52
for i in range(100):
    if "3" in str(i):
        print(i)

#problem53
num = 1
count = 0
while count < 100:
    if "3" in str(num):
        print(num)
        count += 1
    num = num + 1

#problem54
list_2d = [[1,2,3],[4,5,6],[7,8,9]]
x = 0
for i in list_2d:
    y = 0
    for j in i:
        list_2d[x][y] = 2 * j
        y += 1
    x += 1
print(list_2d)

#problem55
x = [[f"{i}-{j}" for j in range(10)] for i in range(10)]
print(x)

#problem56
ascii_dict = {"0*30": "0","0*40": "@","0*50": "P"}
new_dict = {k:v for v,k in ascii_dict.items()}
print(new_dict)

#problem57
target_text = "hello"
count_dict = {}

for char in target_text:
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1
print(count_dict)

#problem58
target_list = [1,2,3,None,5,None,7]
new_list = []
for item in target_list:
    if item is not None:
        new_list.append(item)
print("&".join(new_list))

#problem59
lst = [1, 2, 3, None, 5]
new_list = [x * 2 for x in lst if x is not None]
print(new_list)

#problem60
employees = [
    {'id': '0001', 'name': '田中', 'location_id': 'L01'},
    {'id': '0002', 'name': '山田', 'location_id': 'L02'},
    {'id': '0003', 'name': '小林', 'location_id': 'L01'},
    {'id': '0004', 'name': '藤本', 'location_id': 'L03'},
    {'id': '0005', 'name': '佐々木', 'location_id': 'L02'},
    {'id': '0006', 'name': '松田', 'location_id': 'L04'},
    {'id': '0007', 'name': '中村', 'location_id': 'L01'},
    {'id': '0008', 'name': '石川', 'location_id': 'L03'},
    {'id': '0009', 'name': '清水', 'location_id': 'L05'},
    {'id': '0010', 'name': '近藤', 'location_id': 'L02'}
]
for i in range(len(employees)):
    if employees[i]['location_id'] == 'L01' or employees[i]['location_id'] == 'L02':
        print(employees[i]["id"],employees[i]['name'])
