sum=0
n=int(input("Enter the number "))
i=n
while i>0:
    rem=i%10
    sum=sum+(rem**3)
    i=i//10
    
if n==sum:
    print(f"{n} is an Amstrong Number")
else:
    print(f"{n} is not an Amstrong Number")
    
    
