#WAS to enter any number and check it is palindrum number or not.
#Name : Laxman Sirvi
#Date : 09-03-22
n=int(input("Enter any value : "))
sum=0
t=n
while n>0:
    x=n%10
    sum=sum*10+x
    n=n//10
if(t==sum):
    print("{} is a palimdrome number.".format(t))
else:
    print("{} is a not palimdrome number.".format(t))
