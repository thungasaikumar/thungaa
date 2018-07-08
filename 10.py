x=input()
if x.isalpha():
    print("Invalid")
else:
    x=int(x)
    c=0
    while x!=0:
        x=int(x/10)
        c=c+1
    print(c)
