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