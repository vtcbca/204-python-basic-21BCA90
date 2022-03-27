'''WAS to enter any number to print following pattern

     *
    **
   ***
  ****
 *****
 #Name : Laxman Sirvi
 #Date : 09-03-22'''
n=int(input("Enter No. of rows : "))
k=2*n-2
for i in range (n):
    for j in range (k):
        print(end=" ")
    k=k-2
    for j in range (i+1):
        print("* ",end="")
    print("")
        
