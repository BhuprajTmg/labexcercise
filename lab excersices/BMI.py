#6.solve each of folloeomg problems using ython script . Make sure use appropriate variable name and comments.
# when there is a final answer print th final result it to a the screen.
#A person body mass index is defined as
#BMI=mass in KG/(height in meter)**2

height=float(input("enter your height in feet:"))
height1=0.3048*height
print(f"your height in meter is {height1} M.")
weight=float(input("enter your weight in KG:"))
BMI=weight/height1**2
print("Your BMI is:",BMI)