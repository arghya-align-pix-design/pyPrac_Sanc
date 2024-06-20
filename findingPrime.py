import numpy as np
ip=eval(input("Enter the number to check prime or not: "))
flag=True

for i in range(2,ip-1):
    if(ip%i==0) :
      flag= False

if(flag==True):
 print(ip, "Is a Prime Number ")
else:
  print(ip," is not prime")