#10.Write the program to convert seconds to day, hours, minutes, and seconds.

sec=int(input("Enter the total seconds:"))
day=(((sec//60)//60)//24)
print(f"the total day for given second is {day} day")
hour=((sec//60)//60)
print(f"the total day for given second is {hour} hour")
minute=(sec//60)
print(f"the total minute for given second is {minute} minute")

