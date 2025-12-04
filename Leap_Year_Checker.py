#Taking input of the year from the user
year=int(input("Enter your year to check ::"))

#Giving the conditions of leap year
if (year%4==0 and year%100!=0) or year%400==0:
    print("Yes!",year,"is a leap year.")
else:
    print("OOPs!",year,"is not a leap year")