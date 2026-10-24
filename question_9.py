# Q9 [Advanced] What happens when a set is created from [1,2,[3,4]]? Explain.

a = {1,2,[3,4]}
print(a)

# output is---
# typeerror: cannot use list as a set element (unhashable types)
# Unhashable ka matlab: Aisi cheez jise Python set ke andar store nahi kar sakta ya dictionary ki key nahi bana sakta.


a = {(1, 2), (3, 4)}
print(a)