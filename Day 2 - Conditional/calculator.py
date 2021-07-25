print("Enter 1 for addition")
print("Enter 2 for subraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
n=int(input())

a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))

if n==1:
    c=a+b
    print(f"{a}+{b}={c}")
elif n==2:
    c=a-b
    print(f"{a}-{b}={c}")
elif n==3:
    c=a*b
    print(f"({a})({b})={c}")
elif n==4:
    c=a/b
    print(f"{a}/{b}={c}")
else:
    print("Invalid number")
    

    


