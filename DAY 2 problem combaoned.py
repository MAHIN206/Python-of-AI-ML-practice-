# Problem 3: Print Numbers

N = int(input())

for i in range(1, N + 1):
    print(i)


# Problem 4: Count Even Numbers

N = int(input())
numbers = input().split()

count = 0

for i in range(N):
    if int(numbers[i]) % 2 == 0:
        count += 1

print(count)




N = int(input())

total = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        continue
    total += i

print(total)