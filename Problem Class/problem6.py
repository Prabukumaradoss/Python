n="ocean"
for i in range(len(n)):
    if i%2==0:
        print(chr(ord(n[i])-32),end="")
    else:
        print(n[i],end="")
