# Program to find the simple interest based upon number of years.
# If number of years is more than 12 rate of interest is 10 otherwise 15

p = int(input ( "enter a amount in rupees : "))
t = int(input ("enter a tme period for taking a rupees : "))

if t>12 :
    S=(p*10*t)/100
else :
    S=(p*15*t)/100

print("total simple interest is : " , S )
