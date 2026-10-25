#Separate a mixed list into integer, float, string, and Boolean lists. 

data = [2, 22.6, "hello","krish", 4, 3.6, True, False]


integers = []
floats = []
strings = []
booleans = []

for item in data:

    if type(item) == int:
        integers.append(item)

    
    elif type(item) == float:
        floats.append(item)

    elif type(item) == str:
        strings.append(item)

    elif type(item) == bool:
        booleans.append(item)



print("integers:", integers)
print("floats:", floats)
print("strings:", strings)
print("booleans:", booleans)

