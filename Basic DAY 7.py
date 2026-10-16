file = open("./sample_data/sample.txt", "r")

content = file.read()

print(type(content))

file.close()

print(file.closed)

file = open("./sample_data/sample.txt", "r")

content = file.readlines()

content = list(map(str.strip, content))

filter_content = list(filter(lambda x: len(x) >= 1, content))

print(filter_content)

file.close()

with open("./sample_data/sample.txt", "r") as file:
    content = file.readlines()
    print(content)

print(file.closed)

with open("./sample_data/sample.txt", "r") as file:
    for line in file:
        l = line.strip()
        print(l)

with open("./sample_data/test.txt", "w") as file:
    file.write("Hello test file\n")
    file.write("How is learning going on ?")

with open("./sample_data/test.txt", "w") as file:
    file.write("Second attempt\n")
    file.write("learning is going fast\n")

with open("./sample_data/test.txt", "a") as file:
    file.write("The learning of AI/ML is fun\n")
    file.write("I am enjoying the classes")

strings = ["hello", "hi", "good bye", "what up"]

with open("./sample_data/test2.txt", "a") as file:
    file.writelines(strings)

with open("./sample_data/sample.txt", "r") as file:
    print(file.tell())
    print(file.read())
    print(file.tell())
    print(file.read())

with open("./sample_data/sample.txt", "r") as file:
    print(file.tell())
    print(file.read(5))
    print(file.tell())
    print(file.read())
    print(file.tell())

with open("./sample_data/sample.txt", "r") as file:
    print(file.tell())
    print(file.read(5))
    print(file.tell())
    file.seek(0)
    print(file.tell())
    print(file.read(5))

from functools import reduce

with open("./sample_data/sample.txt", "r") as file:
    string_list = file.readlines()

    total_lines = len(string_list)

    number_of_words = list(
        map(lambda x: len(x.split()), string_list)
    )

    total_number_of_words = reduce(
        lambda x, y: x + y,
        number_of_words,
        0
    )

    string_list = list(map(str.strip, string_list))

    string_list = list(
        map(lambda x: x.replace(" ", ""), string_list)
    )

    number_of_character =