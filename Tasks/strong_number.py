a=int(input("Enter a Number to check: "))
n=a
product=1
sum=0
while a!=0:
    b=a%10
    product=1
    for i in range(1,b+1):
        product*=i
        if i==b:
            sum+=product
    a//=10
if sum==n:
    print("It is a strong number")
else:
    print("It is not a strong number")
