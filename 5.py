a=float(input("enter first number:\n"))
b=float(input("enter second number:\n"))
c=float(input("enter third number:\n"))
if(a>b) and (a>c):
    largest=a
elif(b>a) and (b>c):
    largest=b
else:
    largest=c
print("The largest is:",largest)
