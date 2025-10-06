n = int(input("Enter any number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i == 0 or i == n//2) or i == n-1:
            print("B",end=" ")
        elif(j == 0 or j == n-1):
            print("B",end=" ")
        else:
            print(" ",end=" ")
    print()