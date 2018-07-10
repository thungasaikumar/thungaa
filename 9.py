x=input()
y=input()
s=0
if x.isalpha() or y.isalpha():
    print("Invalid")
else:
    x=int(x)
    y=int(y)
    arr=[int(input()) for _ in range(x)]
    for i in range(y):
        s=s+arr[i]
    print(s)
