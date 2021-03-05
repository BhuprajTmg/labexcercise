#A school decided to replace the desk in three classroom. Each desk sits two students.
#given the number of students in each class, print thr smallest possible number of desk that can be purchased.
#the program should read three integer : the number of student in eash of the three classes , a ,b and c respectively.
#In the first test there are three groups. the firse group has 20 students and tus needs 10 desks. the secomd group has
# student, so they can get by with fewer than  desks.11 deska are also enought for the third group of 22 students.
#So we need  desks in total.


class1=int(input("enter the no. of student:"))
class2=int(input("enter the no. of student:"))
class3=int(input("enter the no. of student:"))
choose1=input("choose class1,class2,class3").lower()

if choose1==class1:
    n_D_of_desk = class1 // 2
    print(f"the number of desk required in class1 is: {n_D_of_desk}")

elif choose1==class2:
    n_D_of_desk = class2// 2
    print(f"the number of desk required in class1 is: {n_D_of_desk}")

else:
    n_D_of_desk = class3 // 2
    print(f"the number of desk required in class1 is: {n_D_of_desk}")







