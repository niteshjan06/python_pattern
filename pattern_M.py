n = int(input("Enter any number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i == j and j <= n//2):
            print("M",end=" ")
        elif(i + j == n-1 and i <= n//2):
            print("M",end=" ")
        elif(j == 0 or j == n-1):
            print("M",end=" ")
        else:
            print(" ",end=" ")
    print()