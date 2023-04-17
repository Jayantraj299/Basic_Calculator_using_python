import tkinter
a = int(input("plese enter your first number = "))

while True:
    b = input("+ = add\n""- = subtract\n""* = multiply\n""/ = devide\n""choose one type of calculation you want to do = ")
    if b == "+":
         print(a , "+")
         break
    elif b == "-":
         print(a , "-")
         break
    elif b == "*":
         print(a , "*")
         break
    elif b == "/":
         print(a , "/")     
         break
    else:
        print ("Wrong try again")           

c = int(input("plese enter your second number = "))

if b == "+":
    print(a,b,c,"=",a+c)    
elif b == "-":
    print(a,b,c,"=",a-c)
elif b == "*":
    print(a,b,c,"=",a*c)
elif b == "/":
    print(a,b,c,"=",float(a/c))    
