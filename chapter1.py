print("Hello world, i am learning python!!!")

#printing variables
var=7000
sal=10000
salInf=200.0
print("My salary is :",var)

#printing with end and sep arguments
print("My previous Salary was: ", end="")
print(var)
print(end="My new Salary is :",)
print(sal)

#types of variables
print("type of sal is: ", type(sal))
print ("Type of salInf",type(salInf))

#taking Input from users
ip=eval(input("Give the number of inputs u wanna enter, i will provide their types:\n"))
for i in range(0,ip):
    vars=eval(input("Enter your data:"))
    print("type is", type(vars))
