line = input()
words = line.split()
res = []

for word in words:
    if word[0].lower() in "aeiou":
        res.append(word)

print(res)