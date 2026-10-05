phone_number = 456249
print(phone_number)

name = "Phitron"
print(name)

age = 20
height = 5.6
name = "Akash"
is_passed = True

print(type(age), type(height), type(name), type(is_passed))

age = 20.5
print(type(age))


name = input("What is your name? ")
print(name)

age = input("Age ?")
print(age, type(age))

age = input("Age ?")
age = int(age)
print(age, type(age))

height = input("Height ?")
print(height, type(height))

height = float(input("Height ?"))
print(height, type(height))

height = height + 0.2
print(height)


x = 10
y = 3

sum = x + y
sub = x - y
mult = x * y
div = round(x / y, 2)
rem = x % y

print(sum, sub, mult, div, rem)


x = 10
y = 3

greater_than = x > y
greater_than_equal = (10 >= 10)

print(greater_than, greater_than_equal)

less_than = x < y
less_than_equal = (10 <= 10)

print(less_than, less_than_equal)

equal = x == y
print(equal)

not_equal = x != y
print(not_equal)


x = 10
y = 5
z = 3

result = (x > y) and (x > z)
print(result)


x = 10
y = 5
z = 15

result = (x > y) and (x > z)
print(result)


x = 10
y = 5
z = 15

result = (x > y) or (x > z)
print(result)


x = 10
y = 20
z = 15

result = (x > y) or (x > z)
print(result)


eq = 10 + 10 / 2 - 5 * 2
print(eq)

eq = (10 + 10) / 2 - 5 * 2
print(eq)