a=input("Enter the string")
print(f"Total length of string is {len(a)}")
vowels=0
spl=0
constants=0
digits=0
alphabet = 0
for i in a:
    if i.isdigit():
        digits+=1
    elif i in '!@#$%^&*':
        spl+=1
    elif i in 'aeiou':
        vowels+=1
    elif i.isalpha():
        alphabet +=1
        
    else:
        constants+=1
        
print(f"No. of vowels in the string is {vowels}")
print(f"No. of constants in the string is {constants}")
print(f"No. of special charcters in the string is {spl}")
print(f"No. of digits in the string is {digits}")
print(f"No. of alphabet in the string is {alphabet}")
