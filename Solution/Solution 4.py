#WAS enter 3 number and print which number maximum number
#Name : Laxman Sirvi
#Date : 09-03-22
n1=int(input("Enter value of No.1 : "))
n2=int(input("Enter value of No.2 : "))
n3=int(input("Enter value of No.3 : "))
if n1>n2 and n1>n3:
    print("{} is the maximum number".format(n1))
elif n2>n1 and n2>n3:
    print("{} is the maximum number".format(n2))
else:
    print("{} is the maximum number".format(n3))

