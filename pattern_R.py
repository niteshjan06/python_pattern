n = int(input("Enter any number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i == 0 or i == n//2 or (i >= n//2 and i==j)):
            print("R",end=" ")
        elif((i <= n//2 and j == n-1) or j == 0):
            print("R",end=" ")
        else:
            print(" ",end=" ")
    print()