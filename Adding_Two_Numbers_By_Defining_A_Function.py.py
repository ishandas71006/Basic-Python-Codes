#Defining a function named "sumoftwonumbers" which adds two numbers
def sumoftwonumbers(num1,num2):
    sum = num1 + num2
    return sum

n1 = float(input("Enter your 1st number :"))
n2 = float(input("Enter your 2nd number :"))

#Calling the function

add=sumoftwonumbers(n1,n2)
print("Addition of the two numbers",n1 , "+",n2,"is",add)