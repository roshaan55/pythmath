import pythmath

x = 7
x1 = -7

print(pythmath.isnegative(x))  # returns False
print(pythmath.isnegative(x1))  # returns True

# Logical Implementation
if pythmath.isnegative(x):
    print("Number", x, "is a negative number")
else:
    print("Number", x, "is not a negative number")

if pythmath.isnegative(x1):
    print("Number", x1, "is a negative number")
else:
    print("Number", x1, "is not a negative number")
