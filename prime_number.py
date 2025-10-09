n = int(input("Enter any number: "))
sum = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if(i%j == 0):
            count += 1
    if(count == 2):
        sum += i
print(f"The sum of The prime numbers is {sum}")