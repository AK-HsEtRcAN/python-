str= input ("enter a string ")
len=int (len(str))
upper=0
lower=0
i=0

while i<len :
    if (str[i]>='a' and str[i]<='z'):
        lower =lower +1
    elif  (str[i]>='A' and str[i]<='Z'):
        upper = upper+1
    i+=1

print("lowercase count : ",lower)
print("uppercase count : " , upper )
