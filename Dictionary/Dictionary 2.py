x={"a":1,"b":2,"c":3,"d":4}
A=input("Enter the Key")
if A in x:
    print(x)
elif A not in x:
    x.update({A:input("Enter the value")})
    print(x)
