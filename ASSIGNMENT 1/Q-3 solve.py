text = "Python is a wonderful language for machine learning"

with open("data.txt", "w") as file:
    file.write(text)
    import string

with open("data.txt", "r") as file:
    txt_file = file.read()

for i in string.punctuation:
    txt_file = txt_file.replace(i, "")

word = txt_file.split()
longest_word = ""
count = 0
for i in word:
    if len(i) > count:
        count = len(i)
        longest_word = i

print(longest_word)