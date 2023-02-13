# WAP to find the largest number in three number

num1 = int(input("Enter the value of num1"))
num2 = int(input("Enter the value of num2"))
num3 = int(input("Enter the value of num3"))

if (num1 > num2) and (num1 > num3):
    print("num1 is greater")
elif (num2 > num3) and (num2 > num1):
    print("num2 is greater")
else:
    print("num3 is greater")
