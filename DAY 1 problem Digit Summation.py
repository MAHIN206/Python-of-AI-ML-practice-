inp = input()

numbers = inp.split() #here we split the input string into a list of strings based on whitespace

x = int(numbers[0]) # 13

y = int(numbers[1]) # 12 

last_digit_of_x = x % 10 
last_digit_of_y = y % 10 

sum = last_digit_of_x + last_digit_of_y 

print(sum)