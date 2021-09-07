a=int(input("Enter the number"))
for i in range(2,a):
    if a%i==0:
        print("It is not a prime number")
        break
else:
    print("It is a prime number")
