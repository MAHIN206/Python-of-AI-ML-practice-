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