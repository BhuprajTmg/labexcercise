#Q3. N student takes K apples and distribute them among each other evenly.The remaning (the undivisible)
#part remains in the basket. How many apple will each single student get? How many apples will be remains in the baske?
# The program reads the number N and K. It should print the two answrer for the above question.

N=int(input("enter the number of apple in the basket:"))
K=int(input("enter the number of apple in the basket:"))

D=K/N
R=K//N

print("the no of apple each student get is",D)
print("the number of apple remains in the basket is ", R)
