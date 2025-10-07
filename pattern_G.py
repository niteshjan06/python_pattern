n = int(input("Enter any number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i == 0 or i == n-1 or(j == n-1 and i>=n//2)):
            print("G",end=" ")
        elif(i == n//2 and j >= n//2):
            print("G",end=" ")
        elif(j == 0):
            print("G",end=" ")
        else:
            print(" ",end=" ")
    print()