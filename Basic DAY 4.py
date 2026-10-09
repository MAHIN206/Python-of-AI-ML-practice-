tup = (10, 20, 30, 40)
float_tup = (10.5, 10.2)
mixed_tup = (10, 10.5, "str", True)

lst = [10, 20, 30]
tup1 = tuple(lst)
print(type(tup1), tup1)

tup = (10, 20, 30, 10.5, "str", False)
print(tup[3])
new_tup = tup[0:3]
print(new_tup)

lst = [10, 20, 30, 40]
lst.append(60)
lst[1] = 100
print(lst)

tup = (10, 20, 30, 40)
try:
    tup[1] = 100
except TypeError as e:
    print("TypeError:", e)
print(tup)

tup = (10, 20, 30, 40, 10, 20, 30, 10)
print(tup.count(10))
print(tup.index(40))

A = {1, 2, 3}
print(type(A), A)

B = []
print(type(B))

C = ()
print(type(C))

S = set()
print(type(S))

S = {1, 2, 3, 4, 1, 2}

if 10 in S:
    print("10 is present")
else:
    print("not present")

total = 0
for element in S:
    total += element
print(total)

s = {5, 1, 2, 4, 3}
s.add(10)
s.add(0)
print(s)

s.pop()
s.pop()
print(s)

try:
    s.remove(5)
except KeyError:
    print("5 was already removed by pop()")
print(s)

a = {1, 2, 3}
b = {1, 2, 5, 6, 4}

print(a.union(b))
print(a.intersection(b))
print(a.isdisjoint(b))
print(a.issubset(b))

dic = {}
print(type(dic))

dic = {"name": "Phitron", "age": 20, "address": "Dhaka", "numbers": [10, 20, 30]}
print(type(dic), dic)

print(dic["numbers"])
print(dic.get("age"))

dic["name"] = "Phitron AI/ML"

dic = {"name": "Phitron", "age": 20, "address": "Dhaka", "numbers": [10, 20, 30], "age": 30}
print(dic)

print(dic)
print(dic.get("math_marks"))
print(dic.get("math_marks", 0))

dic = {"name": "Phitron", "age": 20, "address": "Dhaka", "numbers": [10, 20, 30], "age": 30}

print(dic)
dic["math_marks"] = 30
print(dic)
dic.update({"english_marks": 40})
print(dic)

del dic["math_marks"]
print(dic)

dic_2 = dic.copy()
print(dic_2)

try:
    dic_3 = {{"name": "adil", "age": 20}: 20}
    print(dic_3)
except TypeError as e:
    print("TypeError:", e)

dic = {"name": "Phitron", "age": 20, "address": "Dhaka", "numbers": [10, 20, 30], "age": 30}

keys = dic.keys()
print(keys)

dic["math_numebers"] = 30
print(keys)

values = dic.values()
print(values)

dic["math_numebers"] = 40
print(values)

items = dic.items()
print(items)

for key, value in dic.items():
    print(key, value)

square = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(square)

Co_ordinates = [(10, 10.5), (20.5, 192), (101, 102)]
Locations = ["dhaka", "chattogram", "sylhet"]

exact_location = {co_or: loc for co_or, loc in zip(Co_ordinates, Locations)}
print(exact_location)