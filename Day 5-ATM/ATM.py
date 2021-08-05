print("Welcome to ATM")
balance=10000
pin=12345
PIN=int(input("Enter The PIN NUMBER"))
if pin==PIN:
    print("1. Balance")
    print("2. Credit")
    print("3. Debit")
    n=int(input("Enter your option: "))
    if n==1:
        print(balance)
    elif n==2:
        a=int(input("Enter deposit Amount: "))
        balance+=a
        b=int(input("To know your balance enter 1: "))
        if b==1:
            print(balance)
        else:
            print(f"{a}has been credited to ur account")
    elif n==3:
        a=int(input("Enter Withdraw Amount: "))
        if a<balance:
            balance-=a
            b=int(input("To know your balance enter 1: "))
            if b==1:
                print(balance)
            else:
                print(f"{a}has been debited from ur account")
        else:
            print("Insufficient Balance")
    else:
        print("Enter Crt Option")
else:
    print("Enter Crt PIN NUMBER")






