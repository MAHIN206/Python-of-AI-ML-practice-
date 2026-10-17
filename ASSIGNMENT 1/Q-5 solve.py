word=input()
copy=word.lower()
reverse=""
while len(copy)>0 :
    digit=copy[-1]
    reverse=reverse+digit
    copy=copy[:-1]
if word.lower()!=reverse:
    print("Not Palindrom")
else:
    print("Palindrom")