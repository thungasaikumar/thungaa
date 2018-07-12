p,q=input().split()
p=int(p)
q=int(q)
z=[]
for i in range(p+1,q):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=c+1
    if c==0:
        z.append(i)
x=len(z)
for i in range(0,x):
    if(i==x-1):
        print(z[i])
    else:
        print(z[i],end=' ')
        
        
