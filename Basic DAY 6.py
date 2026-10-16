# Structure of a function

def welcome_message():
  print("hello user")

welcome_message()

def welcome_message(user="None"):
  print(f"hello {user}")

welcome_message("Phitron")

def adder(a,b) :

  """
  add two numbers

  a-> int
  b->int


  """
  sum = a+b
  return sum



m = adder(10,30) * 5

print(m)

help(adder)

help(print)



# Different type of argument

def adder(a,b,c) :
  print(f"{a},{b},{c}")


adder(10,30,20)

def adder(*args) :
  for i in args:
    print(i)


adder(10,30,20,40)

def adder(a=10,b=30,c=10) :
  print(f"{a},{b},{c}")


adder()

def adder(**kwargs):
  for key,value in kwargs.items():
    print(f"{key}: {value}")

adder(a = 10 , b=30 , c = 40 , n_estimator=50)



# Return type

def welcome_message():
  print("hello user")

print(type(welcome_message()))

def adder(a,b) :
  sum = a+b
  return sum

print(type(adder(10,20)))

def adder(a,b) :
  sum = a+b
  return sum

print(type(adder(10.5,20)))

def welcome_message(user="None"):
  return f"hello {user}"

print(type(welcome_message()))



# iterator

s = {10 , 20 , 30 , 40 , 50 }
