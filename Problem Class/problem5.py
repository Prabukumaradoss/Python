n=input().strip()
m=len(n)
count=1
for i in range(m-1):
    if n[i]==n[i+1]:
        count+=1
    else:
        print(n[i]+str(count),end="")
        count=1
print(n[i]+str(count),end="")
