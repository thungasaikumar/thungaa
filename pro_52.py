x=[0,0,0,0]
y=[0,0,0,0]
c=0
x[0],y[0]=input().split()
x[1],y[1]=input().split()
x[2],y[2]=input().split()
x[3],y[3]=input().split()
for i in range(0,4):
    for j in range(1,4):
        if int(x[i])-int(x[j])==0:
           x[i]=0
           x[j]=0
        if int(y[i])-int(y[j])==0:
           y[i]=0
           y[j]=0
for i in range(0,4):
    if int(x[i]!=0) or int(y[i]!=0):
    	c=c+1
if(c==0):
    print("yes")
else:
    print("no")
