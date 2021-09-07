a="arrb7??5xbl8??eee4"
b=""
print(a)
for i in a:
    if i.isalpha():
        continue
    else:
        b+=i
print(b,end="  ")
for i in range(len(b)-1):
    if(b[i] == '?' and b[i+1] == '?'):
        b1=b[i-1]
        b2=b[i+2]
        add=int(b1)+int(b2)
        print(add)
        if(add == 12):
            print(True)
        
    
