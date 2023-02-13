a = "abc"

try:
    print(int(a))
except ValueError:
    print('Please pass integer values')
except IndexError:
    print("please choose index less than the stirng")

except Exception:
    print("Internal server error")
