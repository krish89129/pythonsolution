# Q9 Check whether a number is a power of two using bitwise operators.

n = int(input("enter a number: "))

if (n > 0) and (n & (n-1)) == 0:

    print("power of two")

else:
    print("not a power of two")    


