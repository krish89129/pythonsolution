# Q39 Convert a decimal number stored as a string to integer without using float().

a = "12.8"

result = int(a.split(".")[0])

print(result)


# result = int(a.split('.')[0])

# split('.') string ko decimal point se split karta hai.
# [0] decimal point se pehle wala part select karta hai.
# int() us string ko integer mein convert karta hai.
# result mein final integer value store hoti hai.


a = ('12.4')
print(type(a))