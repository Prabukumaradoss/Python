n=int(input("Enter the number "))
sum=0
i=1
while i<n:
    rem = n%i
    if rem==0:
        sum=sum+i
    i=i+1
if n==sum:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
    
