p,q=input().split()
p=int(p)
q=int(q)
z=[]
for i in range(p+1,q):
    if i%2!=0:
        z.append(i)
x=len(z)
for i in range(0,x):
    if(i==x-1):
        print(z[i])
    else:
        print(z[i],end=' ')
