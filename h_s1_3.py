n=int(input())
a=[0,0,0,0,0,0,0,0,0,0,0]
a=[int(i) for i in input().split()]
for i in range(0,n):
    c=0
    for j in range(0,n):
        if(i!=j):
        	if(a[i]==a[j]):
        		c=c+1
    if c==0:
    	print(a[i])
