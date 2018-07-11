p,q=input().split()
p=int(p)
q=int(q)
for i in range(p+1,q):
    x=i
    c=0
    while(x!=0):
        d=x%10
        c=c+(d*d*d)
        x=int(x/10)
    if(c==i):    
        print(i)
