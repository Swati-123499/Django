_range = int(input())
for i in range(_range):
    n = i
    temp = n
    temp_size = n
    length = 0
    sum = 0
    # is to final length n

    while temp_size > 0:
        temp_size = int(temp_size/10)
        length += 1
        # to find sum
        while n > 0:
            rem = n % 10
            sum += (rem**length)
            n = int(n/10)
        # to compare
    if (temp == sum):
        print(f"{temp} is armstrong")
    else:
        print(f"{temp} is not armstrong")

    while n > 0:
        rem = n % 10
        sum += (rem*rem*rem)
        n = int(n/10)
    if temp == sum:
        print(f"{temp} is armstrong")
    else:
        print(f"{temp} is not armstrong")
