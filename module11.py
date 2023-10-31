#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ASUS
#
# Created:     16/07/2023
# Copyright:   (c) ASUS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

 # write a program in python to replace the vowels present in string  with # .

str =input("enter a string : ")
i=0
l=len(str)


for i in range (l) :
    if ( str[i]=='A' or str[i]== 'E' or str[i]=="I" or str[i] =="O "or str[i]=="U" or str[i]=='a' or str[i]=='e' or str[i]=='i'or str[i]=="o" or str[i]=="u") :
          str =str.replace(str[i] , "#")
print(str)



