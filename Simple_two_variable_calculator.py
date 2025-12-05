def sum(a,b): #Defining a function for addition
    return a+b

def subs(a,b): #Defining a function for substraction
    return a-b

def mul(a,b):   #Defining a function for multiplication
    return a*b 

def div(a,b):   #Defining a function for division
    return a/b

def exp(a,b):   #Defining a function for exponential calculation
    return a**b

#Taking Input from the user
num1 = float(input("Enter your first number :"))   
num2 = float(input("Enter your second number :"))

#Selecting the operation
op = input("Select your operation + , - , / , ^ , * ::")

#Using if else constructing the main code
if op == "+":
    add=sum(num1,num2)
    print(add)

elif op == "-":
    sub=subs(num1,num2)
    print(sub)

elif op == "*":
    multi=mul(num1,num2)
    print(multi)

elif op == "/":
    divide=div(num1,num2)
    print(divide)

elif op == "^":
    ex=exp(num1,num2)
    print(ex)

else:
    print("OOPs ! Invalid Input")




