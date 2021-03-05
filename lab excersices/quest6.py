#To determine the BMI.

height=float(input("enter the heigh in feet:"))
height1=height*0.3048000
print(f"your height in meter is {height1}m")

weight=float(input("enter your weight in K.G:"))
height2=height1

a=height2**2
BMI=weight/a

print(f"The BMI of your body is {BMI} kg/m2")

