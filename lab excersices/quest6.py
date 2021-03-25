#solve the following problems using python scripts. MAke sure you use appropriate variable names and comments.
#when there is a final answer have oythoon print it to the screen.
#A person's body mass index (BMI) is defined as:
#BMI= mass in kg/(height in m)^2

height=float(input("enter the heigh in feet:"))
height1=height*0.3048000
print(f"your height in meter is {height1}m")

weight=float(input("enter your weight in K.G:"))
height2=height1

a=height2**2
BMI=weight/a

print(f"The BMI of your body is {BMI} kg/m2")

