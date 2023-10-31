
i=0
a=int(input("enter starting  no .  "))
b=int(input("enter ending no .  "))

a>0
b>0
if(a%2==0) :
    a=a+1
elif (b%2==0) :
    b=b-1
sum=0

for i in range (a,b+1 , 2):
    sum=sum+i

print(sum)






