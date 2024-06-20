num =eval(input("Enter the cycles of Fibonacci to work: "))
a=0
b=1
print(a," ", b," ", end='')
for k in range( 3, num+1 ):
    c=a+b
    print(c, " ", end="")
    a=b
    b=c
print("\n Task finished Successfully.")