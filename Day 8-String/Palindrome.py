a=input("ENTER THE STRING")
b=len(a)
count=0
for i in range(b):
    if a[i]==a[-i-1]:
        count+=1
        if count==b:
            print("Palindrome")
    else:
        print("Not a palindrome")
        break

