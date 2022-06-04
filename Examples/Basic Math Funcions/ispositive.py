import pythmath

x = 7
x1 = -7

print(pythmath.ispositive(x))  # returns True
print(pythmath.ispositive(x1))  # returns False

# Logical Implementation
if pythmath.ispositive(x):
    print("Number", x, "is a positive number")
else:
    print("Number", x, "is not a positive number")

if pythmath.ispositive(x1):
    print("Number", x1, "is a positive number")
else:
    print("Number", x1, "is not a positive number")
