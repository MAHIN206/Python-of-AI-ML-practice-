prompt = "what is your name?"

print(prompt)
print(type(prompt))


message = """tell me about yourself ?
what are the issues you've been facing while learning to code ?
How are you tackling them ?
"""

print(message)


string = "hello world"

print(string[7])


first_message = message[0:24]

print(first_message)


print(first_message[-1])
print(first_message[-2])
print(first_message[-3])
print(first_message[-4])
print(first_message[-5])


new_first_message = first_message[::-1]

print(new_first_message)


string = "Welcome to Phitron ML Course , Phitron ML , Hello ML"

processed_string = string.lower()

print(len(string))

print("phitron" in processed_string)

shuru_index = processed_string.find("phitron")
print(shuru_index)

shesh_index = processed_string.rfind("phitron")
print(shesh_index)

count = processed_string.count("phitron")
print(count)

processed_string = string.replace("ML", "AI/ML")

print(processed_string)


prompt = "what is Phitron ?"

tokens = prompt.split()

print(type(tokens))
print(tokens)

sentence = "-".join(tokens)

print(type(sentence))
print(sentence)


name = "Adil"
age = 23
height = 5.1123445

info = f"His name is {name.upper()}. He is {age} years old. He is {height:.3f} feet tall.\n"

print(info)


model_accuracy = 0.83333

print(f"the model accuracy is {model_accuracy}")
numbers = [100, 20, 30, 40, 50, 100, 100]
float_numbers = [10.20, 3.15, 2.4, 2.7, 3.5]
fruits = ['apple', 'orange', 'lichi']
mix = [10, 10.20, 'apple']

list_er_moddhe_list = [[100, 20, 30], [14, 12, 31], [13, 12, 12]]


print(numbers[2])

numbers[2] = 90

print(numbers[2])

new_list = numbers[0:3]

print(new_list)


numbers.append(80)
print(numbers)


numbers.insert(0, 45)
print(numbers)


numbers.pop()

print(numbers)


numbers.remove(100)

print(numbers)


numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)


numbers.sort(reverse=True)

print(numbers)


stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(f"top element : {stack[-1]}")

stack.pop()

print(f"top element : {stack[-1]}")


queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue.pop(0))

print(f"front e {queue[0]}")

queue.pop(0)

print(f"front e {queue[0]}")


even = []

random_list = [x + 10 for x in range(1, 101) if x % 2 != 0]

print(random_list)


fruits = ['apple', 'orange', 'lichi']

upper_fruits = [fruit.upper() for fruit in fruits]

print(upper_fruits)