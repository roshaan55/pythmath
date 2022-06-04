import pythmath

x = 4
x1 = 5
x2 = 6

print(pythmath.iseven(x))  # returns True
print(pythmath.iseven(x1))  # returns False
print(pythmath.iseven(x2))  # returns True

# Logical Implementation
if pythmath.iseven(x):
    print("Number", x, "is an even number")
else:
    print("Number", x, "is not an even number")

if pythmath.iseven(x1):
    print("Number", x1, "is an even number")
else:
    print("Number", x1, "is not an even number")

if pythmath.iseven(x2):
    print("Number", x2, "is an even number")
else:
    print("Number", x2, "is not an even number")
