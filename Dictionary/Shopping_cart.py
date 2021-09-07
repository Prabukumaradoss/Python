x={"Course 1":"ECE","Course 2": "CSE","Course 3":"EEE","Course 4":"Mech"}
def toprint():
    for i in x:
        print(i,end=": ")
        print(x[i])
toprint()
a=int(input("""Enter 1 to add
      2 to delete
      3 to update
      4 to view
      Enter the number:"""))

if a==1:
    x["Course 5"]=input("Enter course: ")
    toprint()
if a==2:
    x.pop(input("Enter Key to delete: "))
    toprint()
if a==3:
    for i in x:
        x.update({input("Enter course No."):input("Enter Course")})
    toprint()
if a==4:
    toprint()
    
