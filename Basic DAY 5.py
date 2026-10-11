

def welcome_message():
    print("hello user")

welcome_message()


def welcome_message(user="None"):
    print(f"hello {user}")

welcome_message("Phitron")
welcome_message()




def adder(a, b):
    """
    add two numbers
    a -> int
    b -> int
    """
    total = a + b
    return total

m = adder(10, 30) * 5
print(m)




def adder(a, b, c):
    print(f"{a},{b},{c}")

adder(10, 30, 20)


def adder(*args):
    for i in args:
        print(i)

adder(10, 30, 20, 40)


def adder(a=10, b=30, c=10):
    print(f"{a},{b},{c}")

adder()


def adder(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

adder(a=10, b=30, c=40, n_estimator=50)




def welcome_message():
    print("hello user")

print(type(welcome_message()))


def adder(a, b):
    total = a + b
    return total

print(type(adder(10, 20)))


def adder(a, b):
    total = a + b
    return total

print(type(adder(10.5, 20)))


def welcome_message(user="None"):
    return f"hello {user}"

print(type(welcome_message()))


s = {10, 20, 30, 40, 50}

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

for i in s:
    print(i)



lst = [x for x in range(500)]

def data_loader(chunk_size, lst):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

x = data_loader(5, lst)

print(next(x))
print(next(x))