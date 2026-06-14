#printing the product of numbers from 1 to userinput or its like a n factorial
num=int(input("enter a number to multiply it untill it reaches 1:"))
product=1
number=1
while number<=num:
    product*=number
    number+=1
print(product)
