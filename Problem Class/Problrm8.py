a=list(input("Enter a word"))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if ord(a[i])>ord(a[j]):
            a[i],a[j]=a[j],a[i]
    print(a[i],end=" ")
