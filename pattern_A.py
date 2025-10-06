n = int(input("Enter any number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i == 0 or i == n//2):
            print("A",end=" ")
        elif(j == 0 or j == n-1):
            print("A",end=" ")
        else:
            print(" ",end=" ")
    print()