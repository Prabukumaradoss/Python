n=input("enter input sentence")
m=n.split()
for i in range(len(m)):
    if i%2==0:
        for j in m[i]:
            print(chr(ord(j)-32),end="")
        print(end=" ")
    else:
        print(m[i],end=" ")
