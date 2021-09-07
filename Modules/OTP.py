import random
OTP=""
for i in range(4):
    b=int(random.random()*10)
    OTP+=str(b)
print(OTP)
def verify():
    a=input("Enter otp")
    if OTP==a:
        print("Otp is verified")
    else:
        print("Enter crt OTP")
        verify()
        
        
verify()
