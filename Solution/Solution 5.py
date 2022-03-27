#WAS to enter any number and print from which number from 0 to 9 it is divisible.
#Name : Laxman Sirvi
#Date : 09-03-22
n=int(input("Enter the number to be divided by : "))
for i in range(1,10):
    if n%i==0:
        print(i)
