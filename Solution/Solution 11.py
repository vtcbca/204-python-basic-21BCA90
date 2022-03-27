#WAS to enter any number and check number is armstrong number or not.
#Name : Laxman Sirvi
#Date : 09-03-22
n=int(input("Enter any value = "))
sum=0
t=n
while n>0:
    x=n%10
    y=x*x*x
    sum=sum+y
    n=n//10
if t==sum:
    print("{} is a Armstrong number.".format(t))
else:
    print("{} is a not Armstrong number.".format(t))
