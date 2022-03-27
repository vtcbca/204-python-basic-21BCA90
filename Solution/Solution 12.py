'''WAS to enter any number to print following pattern

 *
 * *
 * * *
 * * * *
 * * * * *
 #Name : Laxman Sirvi
 #Date : 09-03-22'''
n=int(input("Enter a value of rows : "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("")
