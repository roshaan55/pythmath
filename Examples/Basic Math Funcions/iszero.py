import pythmath

x = 0
x1 = 7

print(pythmath.iszero(x))  # returns True
print(pythmath.iszero(x1))  # returns False

# Logical Implementation
if pythmath.iszero(x):
    print("Number", x, "is a zero number")
else:
    print("Number", x, "is not a zero number")

if pythmath.iszero(x1):
    print("Number", x1, "is a zero number")
else:
    print("Number", x1, "is not a zero number")
