#problem36
tpl = (1,2,3)
print(tpl)
print(tpl[0])

#problem37
tpl = (1,2) + (3,4)
print(tpl)
print(len(tpl))

#problem38
st = {1,2,3}
st.add(1)
print(st)
st = {1,2,3}
st.remove(1)
print(st)

#problem39
x = {1,2,3}
y = {3,4,5}
print(x | y)
print(x & y)

#problem40
st = {1,2,3}
for i in st:
    print(i)

#problem41
dct = {"id": "0001","name": "guest"}
print(dct["name"])

#problem42
for key, values in dct.items():
    print(key, values)

#problem43
print([x for x in range(1,10) if x % 2 == 0])
