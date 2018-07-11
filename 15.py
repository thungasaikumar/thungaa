p,q=input().split()
p=int(p)
q=int(q)
for i in range(p+1,q):
    if i%2==0:
        print(i,end=' ')
