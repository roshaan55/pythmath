# pythmath 0.1
Advance Math Library which performs all the basic and scientific math operations such as cos, sin, tan etc

It is an advanced revised version of built-in math library which helps to perform math operations. It includes the area functions which calculates the **area of square**, **area of triangle**, **area of circle** and **area of rectangle**. **pythmath 0.1** includes functions which are as follows:

## Installation:
```nano
pip install pythmath
```
## For Upgradation(pycamdetector):
```nano
pip install --upgrade pythmath
```

## Basic Math Functions:
1) **absoulte()**
2) **sqare_root()**
3) **cube_root()**
4) **calc_lcm()**
5) **calc_gcd()**
6) **fact()**
7) **intsqrt()**
8) **intcbrt()**
9) **hypotenuse()**
10) **floor()**
11) **ceil()**
12) **floatsum()**
13) **floatabs()**
14) **remainder()**
15) **euc_dist()**
16) **exponential()**
17) **iseven()**
18) **isinteger()**
19) **isodd()**
20) **isprime()**
21) **ispositive()**
22) **isnegative()**
23) **iszero()**

## Area Functions
1) **area_rect()**
2) **area_triangle()**
3) **area_square()**
4) **area_circle()**
5) **perimeter_rect()**

## Trignometric Functions:
1) **deg_to_rad()**
2) **rad_to_deg()**
3) **sin()**
4) **sinh()**
5) **sind()**
6) **cos()**
7) **cosd()**
8) **cosh()**
9) **cosec()**
10) **cosecd()**
11) **cot()**
12) **cotd()**
13) **sec()**
14) **secd()**
15) **tan()**
16) **tand()**
17) **tanh()**


# Basic Math Function Implementation:
## absolute():
It  is the function that gets the absolute value of x, if negative value it will be positive value.

**Example:**
```py
import pythmath

num = -7
print(pythmath.absolute(num))
```
**Output:** 7

## square_root():
It is a function that finds the square root of any number.

**Example:**
```py
import pythmath

num = 25
print(pythmath.square_root(num))
```
**Output:** 5

## cube_root():
It is a function that finds the cube root of a number.

**Example:**
```py
import pythmath

num = 27
print(pythmath.cube_root(num))
```
**Output:** 3

## calc_lcm():
It is a function that calculates the least common multiple of two numbers

**Example:**
```py
import pythmath

a = 10
b = 18

print(pythmath.calc_lcm(a, b))
```
**Output:** 90.0

## calc_gcd():
It is a function that calculates the greatest common divisor of two numbers.

**Example**
```py
import pythmath

a = 20
b = 18

print(pythmath.calc_gcd(a, b))
```
**Output:** 2.0

## fact():
It is a function that calculates the factorial of number.

**Example:**
```py
import pythmath

num = 4

print(pythmath.fact(num))
```
**Output:** 24.0

## intsqrt():
It is a function to get the integer part of square root of a number.

**Examples:**
```py
import pythmath

a = 20

print(pythmath.intsqrt(a))
```
**Output:** 4

## intcbrt():
It is a function to get the integer part of cube root of a number

**Example**
```py
import pythmath

a = 20

print(pythmath.intcbrt(a))
```
**Output**: 2

## hypotenuse():
It is function that calculates the hypotenuse of two numbers.

**Example:**
```py
import pythmath

a = 3
b = 4

print(pythmath.hypotenuse(a, b))
```
**Output:** 5.0

## floor():
It is the function that gets the exact floored value, for example the number is 3.4 it will get 3

**Example:**
```py
import pythmath

a = 3.7

print(pythmath.floor(a))
```
**Output:** 3

## ceil()
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
# area_rect():
It is a function that calculates the area of rectangle.

**Example:**
```py
import pythmath

x = 5
y = 6

print(pythmath.area_rect(x, y))
```
**Output:** 30.0

## perimeter_rect()
It is a function to calculate the perimeter of rectangle.

**Example:**
```py
import pythmath

x = 5
y = 6

print(pythmath.perimeter_rect(x, y))
```
**Output:** 22.0

## area_triangle():
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

## area_square():
It is a function that calculates the area of square.

**Example:**
```py
import pythmath

x = 5

print(pythmath.area_square(x))
```
**Output:** 25.0

## area_circle():
It is a function to calculate the area of circle.

**Example:**
```py
import pythmath

radius = 5

print(pythmath.area_circle(radius))
```
**Output:** 78.53981633974483

## Trignometric Functions:
# sin()
It is function to calculate sine of x or any number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.sin(angle))
```
**Output**: -0.13235175009777303

## sind():
It is a function to calculate sine of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.sind(angle))
```
**Output:** 0.42261826174069944

## sinh():
It is a function to calculate hyperbolic sine of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.sinh(angle))
```
**Output:** 36002449668.69289

## cos():
It is a function to calculate cosine of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cos(angle))
```
**Output:** 0.9912028118634736

## cosd():
It is a function to calculate cosine of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cosd(angle))
```
**Output:** 0.9063077870366499

## cosh():
It is a function to calculate hyperbolic cosine of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cosh(angle))
```
**Output:** 36002449668.69289

## cosec():
It is a function to calculate cosec of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cosec(angle))
```
**Output:** -7.555623550585948

## cosecd():
It is a function to calculate cosec of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cosecd(angle))
```
**Output:** 2.3662015831524985

## cot():
It is a function to calculate cotangent of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cot(angle))
```
**Output:** -7.489155308722674

## cotd():
It is a function to calculate cotangent of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.cotd(angle))
```
**Output:** 2.1445069205095586

## sec():
It is a function to calculate secant of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.sec(angle))
```
**Output:** 1.0088752655170414

## secd():
It is a function to calculate secant of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.secd(angle))
```
**Output:** 1.1033779189624917

## tan():
It is a function to calculate tangent of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.tan(angle))
```
**Output:** -0.13352640702153587

## tand():
It is a function to calculate tangent of a number in degrees.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.tand(angle))
```
**Output:** 0.46630765815499864

## tanh():
It is a function to calculate hyperbolic tangent of a number in radians.

**Example:**
```py
import pythmath

angle = 25

print(pythmath.tanh(angle))
```
**Output:** 1.0

For more examples see [Examples](https://github.com/roshaan55/pythmath/blob/main/examples "Examples of funcions of pythmath").


