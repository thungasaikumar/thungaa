a,b=input().split()
a=int(a)
b=int(b)
n=[int(i) for i in input().split()]
c=int(input())
s=0
for i in range(0,a):
    s=s+n[i]
if s/2==c:
    print(int(n[b]/2))
else:
    print("Bon Appetit")
    
