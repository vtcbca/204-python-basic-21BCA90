'''WAS to enter any number to print following pattern

 *****
  ****
   ***
    **
     *
#Name : Laxman Sirvi
#Date : 09-03-22'''
n=int(input("Enter the No. of rows : "))
for i in range (n+1):
      print(" "*(i+1), end="")
      for j in range (n-i):
            print("*", end="")
      print()
