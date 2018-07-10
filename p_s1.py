a=input()
c=0
b=int(a)
while(b!=0):
    d=b%10
    c=c*10+d
    b=int(b/10)
print(c)
