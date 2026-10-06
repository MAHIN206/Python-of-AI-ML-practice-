taka = 1000
raining = False

if (taka > 500) and (raining == False):
    print("ghurte jabo")
else:
    print("Taka ta save korbo")


for i in range(1, 10):
    for j in range(1, 5):
        print(i, j)


count = 10

while count < 10:
    print(count, "hello world")
    count = count + 1

print(count)


sum = 0

for i in range(1, 11):

    print(i, "is processing")

    if i % 2 == 0:
        continue

    sum += i
    print(i, "is added to the sum")


accuracy = 30

accuracy = 95

changed_or_not = True
prev = accuracy

while True:

    if changed_or_not == False and accuracy == 100:
        break

    if prev > accuracy:
        changed_or_not = False
        print("accuracy is decreased")
        print("accuracy is increased")