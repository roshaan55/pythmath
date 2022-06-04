import pythmath

x = 7
x1 = -7
x2 = 7.6

print(pythmath.isinteger(x))  # returns True
print(pythmath.isinteger(x1))  # returns True
print(pythmath.isinteger(x2))  # returns False

# Logical Implementation
if pythmath.isinteger(x):
    print("Number", x, "is an integral number")
else:
    print("Number", x, "is a non-integral number")

if pythmath.isinteger(x1):
    print("Number", x1, "is an integral number")
else:
    print("Number", x1, "is a non-integral number")

if pythmath.isinteger(x2):
    print("Number", x2, "is an integral number")
else:
    print("Number", x2, "is a non-integral number")
