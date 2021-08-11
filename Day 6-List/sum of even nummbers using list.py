n=[]
sum=0
b=int(input("Ending Range"))
for i in range(0,b):
    n.append(int(input()))
    if n[i]%2==0:
        sum+=n[i]
print(sum)
