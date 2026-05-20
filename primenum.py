n = int(input("Enter number: "))

flag = 0

for i in range(2, n):
    if n % i == 0:
        flag = 1
        break

if flag == 0:
    print("It is a Prime Number")
else:
    print("It is Not a Prime")