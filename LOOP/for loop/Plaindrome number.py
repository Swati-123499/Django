# Wap to find palindrome or not
String = input("Enter a string")

revstr = ""

for i in String:
    revstr = i+revstr
    print("Reverse string:", revstr)

if (String == revstr):
    print("Number is palindrome")
else:
    print("Number is not palindrome")
