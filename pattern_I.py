n = int(input("Enter any number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i == 0 or  i == n-1):
            print("I",end=" ")
        elif(j == n//2):
            print("I",end=" ")
        else:
            print(" ",end=" ")
    print()