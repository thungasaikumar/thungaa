n=int(input())
b=n
c=0
while(b!=0):
    d=b%10
    c=c+(d*d*d)
    b=int(b/10)
if(n==c):
    print("yes")
else:
    print("no")
