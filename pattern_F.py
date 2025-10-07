n = int(input("Enter any number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i == 0 or i == n//2):
            print("F",end=" ")
        elif(j == 0):
            print("F",end=" ")
        else:
            print(" ",end=" ")
    print()