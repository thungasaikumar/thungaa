a=int(input())
c=0
for i in range(1,a):
    if(a%i==0):
        c=c+1
if(c==1):
    print("yes")
else:
    print("no")
