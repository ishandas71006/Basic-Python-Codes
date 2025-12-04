#Taking Input From The User
num=int(input("Enter Your Number Greater Than 0 ::"))

fact=1 #Taking a new variable "Fact" and assigning it's value as 1 

if num>0: #Giving this condition because factorial exists only for positive non zero integers
    
    for i in range(1,num+1):
        print(i,end="*")
        fact=fact*i
    print("=",fact)
    
else:
    print("Error! Please enter a valid input.")
