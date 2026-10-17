def compute_ratio(x, y):
    try:
        x1 = x + y
        x2 = x * y
        return x1 / x2
    except Exception as e:
        print("Error: Division not possible")

x, y = map(int, input().split())
print(compute_ratio(x, y))