n=int(input("Enter the end of series:"))
a=0
b=1
for i in range(n//2):
    print(a,end=" ")
    b=a+b
    print(b,end=" ")
    a=a+b
if n%2!=0:
     print(a,end=" ")
    

