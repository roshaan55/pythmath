# pythmath
Advance Math Library which performs all the basic and scientific math operations such as cos, sin, tan etc

It is an advanced revised version of built-in math library which helps to perform math operations. It includes the area functions which calculates the **area of square**, **area of triangle**, **area of circle** and **area of rectangle**. **pythmath 0.1** includes functions which are as follows:

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
**Output:** 25

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

