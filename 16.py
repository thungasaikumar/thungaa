p,q=input().split()
p=int(p)
q=int(q)
for i in range(p+1,q):
    c=0
    for j in range(1,int(i)):
        if(i%j==0):
            c=c+1
    if(c==1):
        print(i,end=' ')
        
        
