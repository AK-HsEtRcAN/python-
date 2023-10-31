import math
print("1 - square , 2 - rectangle , 3-triangle ")

a=int(input("enter a number : "))
if a==1 :
    b = int (input ("enter a side :") )
    print("area is : " , b*b )

elif a==2 :
     c = int(input ("enter length : "))
     d =int(input ("enter bredth : "))
     print("area is : ", c*d )

elif  a==3 :
     e=(int(input ("enter a side of triangle : ")))
     f=int(input("eenter second side of square : "))
     g=int(input ("enter third side of square : "))

     h=(e+f+g)/2
     i=math.sqrt(h*(h-e)*(h-f)*(h-g))
     print("area is : " , i)

else :
    print("not a valid option ")
