# Q39 Convert a decimal number stored as a string to integer without using float().

a = "12.8"

result = int(a.split(".")[0])

print(result)