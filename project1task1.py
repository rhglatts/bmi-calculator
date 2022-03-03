#Rebecca Glatts
#Project 1

#Task 1

#asks user for choice in BMI system
choice = input("Would you like to use the USA or metric system? Enter u for USA, metric is default \n")

#Asks user for height and weight and shows in and lb if using USA system, and m and kg if using metric system
height = int(input("Enter your height:" + "(in)" if choice == "u" else "Enter your height: (m)"))
weight = int(input("Enter your weight: " + "(lb)" if choice == "u" else "Enter your weight: (kg)"))

#Accounts for dividing by 0 by automatically making the BMI of someone who enters 0 for height 0.0
if height != 0:
    BMI = weight / (height**2)
else: 
    BMI = 0

#If user is using USA metric stystem, the BMI is multiplied by 703 to make it correct
if choice == "u":
    BMI *= 703

#If the BMI is less than 18 it prints it out and tells user they are underweight
if BMI < 18:
    print("BMI is ", BMI, "which is underweight.")
#tells user they are overweight if BMI is over 25
elif BMI > 25:
    print("BMI is", BMI, "which is overweight.")

#If BMI is within normal range, it tells user so 
else: 
    print("BMI is", BMI, "which is normal.")
"""
Testing...

Would you like to use the USA or metric system? Enter u for USA, metric is default 
u
Enter your height:(in)70
Enter your weight: (lb)135
BMI is 19.368367346938776 which is normal.

Would you like to use the USA or metric system? Enter u for USA, metric is default 
m
Enter your height: (m)1
Enter your weight: (kg)70
BMI is 70.0 which is overweight.

Would you like to use the USA or metric system? Enter u for USA, metric is default 
u
Enter your height:(in)86
Enter your weight: (lb)120
BMI is  11.406165494862087 which is underweight.

Would you like to use the USA or metric system? Enter u for USA, metric is default 
m
Enter your height: (m)0
Enter your weight: (kg)30
BMI is  0 which is underweight.

Would you like to use the USA or metric system? Enter u for USA, metric is default 
u
Enter your height:(in)50
Enter your weight: (lb)0
BMI is  0.0 which is underweight.

"""