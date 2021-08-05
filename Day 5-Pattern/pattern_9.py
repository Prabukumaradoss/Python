a=1
for i in range(1,6,1):
    for j in range(5):
        if i==1:
            if a<10:
                print(f" {a}",end=" ")
            else:
                print(f"{a}",end=" ")
            a+=1
        elif i==2:
            a+=2
            if a%2==0:
                if a<10:
                    print(f" {a}",end=" ")
                else:
                    print(f"{a}",end=" ")
        elif i==3:
            a+=3
            if a%3==0:
                if a<10:
                    print(f" {a}",end=" ")
                else:
                    print(f"{a}",end=" ")
                
        elif i==4:
            a+=4
            if a%4==0:
                if a<10:
                    print(f" {a}",end=" ")
                else:
                    print(f"{a}",end=" ")
                
        elif i==5:
            a+=5
            if a%5==0:
                if a<10:
                    print(f" {a}",end=" ")
                else:
                    print(f"{a}",end=" ")
                
    a=0
            
    print()
