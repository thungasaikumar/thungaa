a=int(input())
x=a
c=0
while(x!=0):
    d=x%10
    c=(c*10)+d
    x=int(x/10)
if(a==c):
    print("yes")
else:
    print("no")    
    
