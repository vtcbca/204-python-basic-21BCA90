#WAS to enter any number and print the sum of its digit
#Name : Laxman Sirvi
#Date : 09-03-22
n=int(input("Enter any value : ")) 
sum=0
a=n
while n>0:
    t=n%10
    sum=sum+t
    n=n//10
print("The sum of {}'s all digit is {}".format(a,sum))
