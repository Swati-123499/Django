"""
a, b = 1, 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
"""

num = int(input())
for i in range(num):
    # print(i)
    for j in range(i+1):
        print("*", end="  ")
    print()
"""
N = int(input())
for i in range(1, N):
    print("* "*(i))
print("* " * N, end="")
"""
