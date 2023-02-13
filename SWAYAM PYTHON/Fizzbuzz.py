for i in range(1, 51):
    # print(i)
    if (i % 3 == 0) and (i % 5 == 0):
        print(str(i)+" =FIZZBUZZ")
    elif (i % 3 == 0):
        print(str(i)+"= FIZZ")
    else:
        print(str(i)+"= BUZZ")
