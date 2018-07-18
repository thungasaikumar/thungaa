n,k=input().split()
n=int(n)
k=int(k)
a=[int(i) for i in input().split()]
for i in range(k):
    s=a[n-1]
    for j in range(n):
        a[i]=a[i+1]
        a[0]=s
for i in range(0,n):
    print(a[i])
