n = int(input("Enter any number: "))
for i in range(0,n):
    for j in range(0,n):
        if(j == 0 or  j == n-1):
            print("H",end=" ")
        elif(i == n//2):
            print("H",end=" ")
        else:
            print(" ",end=" ")
    print()