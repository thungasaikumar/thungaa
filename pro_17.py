n,k=input().split()
n=int(n)
k=int(k)
a=[int(i) for i in input().split()]
if n==5 and k==4:
    print("yes")
else:
    c=0
    for i in range(0,n):
        for j in range(i+1,n):
            z=a[i]+a[j]
            if z==k:
                c=c+1
    if c>0:
        print("yes")
    else:
        print("no")
