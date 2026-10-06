a = input().split()

brightness = int(a[0])
threshold = int(a[1])

if brightness >= threshold:
    print("ON")
else:
    print("OFF")