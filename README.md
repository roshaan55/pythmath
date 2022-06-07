# pythmath 0.2
Advance Math Library which performs all the basic and scientific math operations such as cos, sin, tan etc

It is an advanced revised version of built-in math library which helps to perform math operations. It includes the area functions which calculates the **area of square**, **area of triangle**, **area of circle** and **area of rectangle**. **pythmath 0.1** includes functions which are as follows:

## Installation:
```nano
pip install pythmath
```
## For Upgradation(pythmath):
```nano
pip install --upgrade pythmath
```

New upadate **pythmath 0.2** includes new functions such as statistical functions(mean, median, mode, variance) etc and other maths functions.
New updates includes error functions such as percentage error, absolute error and relatable error.

## New Math Functions:
1) **Is Sorted**
2) **Percentage**
3) **Array Sum**
4) **Array 2d Sum**
5) **nCr**
6) **nPr**
7) **Fibonacci Series Function**
8) **Multiply Two List**
9) **Square of List**
10) **Powerd List**
11) **Sort List**
12) **Count List**
13) **Minimum in List**
14) **Maximum in List**

## Basic Math Functions:
1) **Absolute Function**
2) **Square Root Function**
3) **Cube Root Function**
4) **LCM Function**
5) **GCD Function**
6) **Factorial Function**
7) **Integer Square Root Function**
8) **Integer Cube Root Function**
9) **Hypotenuse Function**
10) **Floor Function**
11) **Ceil Function**
12) **Float Sum Function**
13) **Float Absolute Function**
14) **Remainder Function**
15) **Euclidean Distance Function**
16) **Exponential Function**
17) **Is Even Function**
18) **Is Integer Function**
19) **Is Odd Function**
20) **Is Prime Function**
21) **Is Positive Function**
22) **Is Negative Function**
23) **Is Zero Function**

## Area Functions
1) **Area of Rectangle Function**
2) **Area of Triangle Function**
3) **Area of Square Function**
4) **Area of Circle Function**
5) **Perimeter of Rectangle Function**

## Trignometric Functions:
1) **Degrees to Radians Function**
2) **Radians to Degrees Function**
3) **Sin(x) Function**
4) **Sinh(x) Function**
5) **Sind(x) Function**
6) **Cos(x) Function**
7) **Cosd(x) Function**
8) **Cosh(x) Function**
9) **Cosec(x) Function**
10) **Cosecd(x) Function**
11) **Cot(x) Function**
12) **Cotd(x) Function**
13) **Sec(x) Function**
14) **Secd(x) Function**
15) **Tan(x) Function**
16) **Tand(x) Function**
17) **Tanh(x) Function**

## Statistical Functions
1) **Mean**
2) **Median**
3) **Mode**
4) **Standard Deviation**
5) **Mean Absolute Deviation(MAD)**
6) **Variance**
7) **Z Score**
8) **Standard Error**
9) **Sampling Error**
10) **Statistical Range**
11) **Midpoint Range**

## Error Functions:
1) **Percentage Error**
2) **Absolute Error**
3) **Relatable Error**

# New Math Functions:
## Is Sorted:
It is the function to check whether the list is sorted or not, if a list is sorted it will return **True** otherwise **False**.

**Example:**
```py
import pythmath

lst1 = [2, 8, 15, 3, 5]
lst2 = [1, 2, 3, 4, 5]

print(pythmath.is_sorted(lst1))
print(pythmath.is_sorted(lst2))
```
**Output 1:** **False**
**Output 2:** **True**

## Percentage:
It is a function to calculate percentage

**Example:**
```py
import pythmath

print(pythmath.percentage(20, 50))
```
**Output:** 40.0

# Array Sum:
It is a function that calculates the sum of numbers in a **1d Array**.

**Example:**
```py
import pythmath


array = {12, 3, 4, 15}
print(pythmath.arr_sum(array))
```
**Output:** 34

# Array 2d Sum:
It is a function to calculates the sum of numbers in a **2d Array**.

**Example:**
```py
import pythmath


array_2d = [[1, 2],
            [3, 4],
            [5, 6]
            ]
print(pythmath.arr_2d_sum(array_2d))
```
**Output:** 21

# nCr:
It is a function that calculates the Combinations nCr from n a r values.

**Example:**
```py
import pythmath


n = 10
r = 5
print(pythmath.nCr(n, r))
```
**Output:** 252.0

# nPr:
It is a function that calculates Permutations nPr from n and r values.

**Example:**
```py
import pythmath


n = 5
r = 2
print(pythmath.nCr(n, r))
```
**Output:** 20.0

# Fibonacci Series:
It is a function that generates the fibonacci series from n_terms.

# Basic Math Function Implementation:
## Absolute Function:
It  is the function that gets the absolute value of x, if negative value it will be positive value.

**Example:**
```py
import pythmath

num = -7
print(pythmath.absolute(num))
```
**Output:** 7

## Square Root Function:
It is a function that finds the square root of any number.

**Example:**
```py
import pythmath

num = 25
print(pythmath.square_root(num))
```
**Output:** 5

## Cube Root Function:
It is a function that finds the cube root of a number.

**Example:**
```py
import pythmath

num = 27
print(pythmath.cube_root(num))
```
**Output:** 3

## LCM Function:
It is a function that calculates the least common multiple of two numbers

**Example:**
```py
import pythmath

a = 10
b = 18

print(pythmath.calc_lcm(a, b))
```
**Output:** 90.0

## GCD Function:
It is a function that calculates the greatest common divisor of two numbers.

**Example**
```py
import pythmath

a = 20
b = 18

print(pythmath.calc_gcd(a, b))
```
**Output:** 2.0

## Factorial Function:
It is a function that calculates the factorial of number.

**Example:**
```py
import pythmath

num = 4

print(pythmath.fact(num))
```
**Output:** 24.0

## Integer Square Root Function:
It is a function to get the integer part of square root of a number.

**Examples:**
```py
import pythmath

a = 20

print(pythmath.intsqrt(a))
```
**Output:** 4

## Integer Cube Root Function:
It is a function to get the integer part of cube root of a number

**Example**
```py
import pythmath

a = 20

print(pythmath.intcbrt(a))
```
**Output**: 2

## Hypotenuse Function:
It is function that calculates the hypotenuse of two numbers.

**Example:**
```py
import pythmath

a = 3
b = 4

print(pythmath.hypotenuse(a, b))
```
**Output:** 5.0

## Floor Function:
It is the function that gets the exact floored value, for example the number is 3.4 it will get 3

**Example:**
```py
import pythmath

a = 3.7

print(pythmath.floor(a))
```
**Output:** 3

## Ceil Function
It is function that ceil the number.

**Example:**
```py
import pythmath

a = 3.7

print(pythmath.ceil(a))
```
**Output:** 4

For more basic math functions see [Examples/Basic Math Functions](https://github.com/roshaan55/pythmath/tree/main/Examples/Basic%20Math%20Funcions "Examples of basic math functions").

## Area Functions:
# Area of Rectangle Function:
It is a function that calculates the area of rectangle.

**Example:**
```py
import pythmath

x = 5
y = 6

print(pythmath.area_rect(x, y))
```
**Output:** 30.0

## Perimeter of Rectangle Function:
It is a function to calculate the perimeter of rectangle.

**Example:**
```py
import pythmath

x = 5
y = 6

print(pythmath.perimeter_rect(x, y))
```
**Output:** 22.0

## Area of Triangle Function:
It is a function that calculates the area of triangle.

**Example:**
```py
import pythmath

a = 5
b = 6
c = 7

print(pythmath.area_triangle(a, b, c))
```
**Output:** 14.696938456699069

## Area of Square Function:
It is a function that calculates the area of square.

**Example:**
```py
import pythmath

x = 5

print(pythmath.area_square(x))
```
**Output:** 25.0

## Area of Circle Function:
It is a function to calculate the area of circle.

**Example:**
```py
import pythmath

radius = 5

print(pythmath.area_circle(radius))
```
**Output:** 78.53981633974483

## Trignometric Functions:
# Sin(x) Function:
It is function to calculate sine of x or any number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.sin(angle))
```
**Output**: -0.13235175009777303

## Sind(x) Function:
It is a function to calculate sine of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.sind(angle))
```
**Output:** 0.42261826174069944

## Sinh(x) Function:
It is a function to calculate hyperbolic sine of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.sinh(angle))
```
**Output:** 36002449668.69289

## Cos(x) Function:
It is a function to calculate cosine of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cos(angle))
```
**Output:** 0.9912028118634736

## Cosd(x) Function:
It is a function to calculate cosine of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cosd(angle))
```
**Output:** 0.9063077870366499

## Cosh(x) Function:
It is a function to calculate hyperbolic cosine of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cosh(angle))
```
**Output:** 36002449668.69289

## Cosec(x) Function:
It is a function to calculate cosec of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cosec(angle))
```
**Output:** -7.555623550585948

## Cosecd(x) Function:
It is a function to calculate cosec of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cosecd(angle))
```
**Output:** 2.3662015831524985

## Cot(x) Function:
It is a function to calculate cotangent of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cot(angle))
```
**Output:** -7.489155308722674

## Cotd(x) Function:
It is a function to calculate cotangent of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cotd(angle))
```
**Output:** 2.1445069205095586

## Sec(x) Function:
It is a function to calculate secant of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.sec(angle))
```
**Output:** 1.0088752655170414

## Secd(x) Function:
It is a function to calculate secant of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.secd(angle))
```
**Output:** 1.1033779189624917

## Tan(x) Function:
It is a function to calculate tangent of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.tan(angle))
```
**Output:** -0.13352640702153587

## Tand(x) Function:
It is a function to calculate tangent of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.tand(angle))
```
**Output:** 0.46630765815499864

## Tanh(x) Function:
It is a function to calculate hyperbolic tangent of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.tanh(angle))
```
**Output:** 1.0

For more examples see [Examples](https://github.com/roshaan55/pythmath/blob/main/examples "Examples of funcions of pythmath").


