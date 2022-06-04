import pythmath

x = 3
x1 = 4
x2 = 5

print(pythmath.isodd(x))  # returns True
print(pythmath.isodd(x1))  # returns False
print(pythmath.isodd(x2))  # returns True

# Logical Implementation
if pythmath.isodd(x):
    print("Number", x, "is an odd number")
else:
    print("Number", x, "is not an odd number")

if pythmath.isodd(x1):
    print("Number", x1, "is an odd number")
else:
    print("Number", x1, "is not an odd number")

if pythmath.isodd(x2):
    print("Number", x2, "is an odd number")
else:
    print("Number", x2, "is not an odd number")
