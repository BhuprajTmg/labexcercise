#Q3. N student takes K apples and distribute them among each other evenly.The remaning (the undivisible)
#part remains in the basket. How many apple will each single student get? How many apples will be remains in the baske?
# The program reads the number N and K. It should print the two answrer for the above question.
N=int(input("Enter the number of student:"))
K=int(input("Enter the number of apple:"))

N_A=K/N

print(f"the number of apple that each student gets is",N_A)

R_A=K%N

print(f"The number of apple remains in on the basket is",R_A)
