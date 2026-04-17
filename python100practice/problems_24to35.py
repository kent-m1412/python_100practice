#problem24
x = 15
if x > 10:
    print("x is bigger than 10")

#problem25
x = 10
if x > 10:
    print("x is bigger than 10")
elif x > 5:
    print("x is bigger than 5, but smaller than 10")
else:
    print("x is smaller than 5")

#problem26
x = 10
y = 20
print(x > y)
print(x >= y)
print(x == y)
print(x <= y)
print(x < y)

#problem27
lst = [1,2,3]
print(2 in lst)

#problem28
x = None
print(x is None)

#problem29
x = 10
y = 20
print((x > 15) & (y >15))
print((x > 15) | (y > 15))

#problem30
x = None
if x is not None:
    print("x is not None")

#problem31
x = [1,2,3]
for i in x:
    print(i)

#problem32
for x in range(10):
    print(x)

#problem33
x = 5
for i in range(10):
    if i == x:
        break
    print(i)

#problem34
x = 5
for i in range(10):
    if i == x:
        continue
    print(i)

#problem35
x = 10
while x > 0:
    print(x)
    x = x - 1
