# pythmath 0.2
Advance Math Library which performs all the basic and scientific math operations such as cos, sin, tan etc. New functions included in **pythmath 0.2** such as basic statistical functions(**Mean**, **Median**, **Mode**, **Standard Deviation**, **Mean Absolute Deviation(MAD)**, **Variance** etc...), error functions(**Percentage Error**, **Absolute Error**, **Relatable Error**)

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

New math functions and statistic functions added in recent revised version of **pthmath 0.2** version **pythmath 0.2.1** which are **nth Root**, **Harmonic Mean**, **Geometric Mean**, **Median Absolute Deviation**, **Multiply a list**, **Covariance**, **List Prime Factors**, **List of Prime Numbers**, **List of Odd Numbers**, **List of Even Numbers**. 

## New Math Functions:
1) **nth Root**
2) **Multiply a list**
3) **List of Prime Factors**
4) **List of Prime Numbers**
5) **List of Odd Numbers**
6) **List of Even Numbers**

## New Statistics Functions:
1) **Harmonic Mean**
2) **Geometric Mean**
3) **Median Absolute Deviation**
4) **Covariance**

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
24) **Is Sorted**
25) **Percentage**
26) **Array Sum**
27) **Array 2d Sum**
28) **nCr**
29) **nPr**
30) **Fibonacci Series Function**
31) **Multiply Two List**
32) **Square of List**
33) **Powerd List**
34) **Sort List**
35) **Count List**
36) **Minimum in List**
37) **Maximum in List**
38) **Is Float**
39) **Positive or Negative**

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
5) **Population Standard Deviation**
6) **Mean Absolute Deviation(MAD)**
7) **Variance**
8) **Z Score**
9) **Standard Error**
10) **Sampling Error**
11) **Statistical Range**
12) **Mid Range**

## Error Functions:
1) **Percentage Error**
2) **Absolute Error**
3) **Relatable Error**

# New Math Functions:
## nth Root:
It is a function that calculates the n under root or root of nth number.

**Example:**
```py
import pythmath

num = 81
n = 4

print(pythmath.nth_root(num, n))
```
**Output:** 3.0

## Multiply a List:
It is a function that multiplies numbers of a list.

**Example:**
```py
import pythmath

list1 = [1, 2, 3]
list2 = [3, 2, 4]

print(pythmath.multiply_lst(list1))
print(pythmath.multiply_lst(list2))
```
**Output of list1:** 6

**Output of list2:** 24

## List of Prime Factors:
It is a function that gets the prime factors of a number, if a number is 100 it will get [2, 2, 5, 5].

**Prime Factors:** prime factor is finding which prime numbers multiply together to make the original number.

**Example:**
```py
import pythmath

num = 100

print(pythmath.prime_factors(num))
```
**Output:** [2, 2, 5, 5]

## List of Prime Numbers:
It is a function that generates a list of prime numbers from starting range to ending range.

**Example:**
```py
import pythmath

start = 1
end = 20

print(pythmath.prime_numbers(start, end))
```
**Output:** [1, 2, 3, 5, 7, 11, 13, 17, 19]

## List of Even Numbers:
It is a function that generates a list of even numbers from starting range to ending range.

**Example:**
```py
import pythmath

start = 1
end = 20

print(pythmath.even_numbers(start, end))
```
**Output:** [1, 2, 4, 6, 8, 10, 12, 14, 16, 18]

## List of Odd Numbers:
It is a function that generates a list of odd numbers from starting range to ending range.

**Example:**
```py
import pythmath

start = 1
end = 20

print(pythmath.odd_numbers(start, end))
```
**Output:** [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# New Statistics Functions:
## Harmonic Mean:
It is a function that calculates the harmonic mean from given dataset, list of numbers or tuple of numbers.

**Harmonic Mean:** In mathematics, the harmonic mean is one of several kinds of average, and in particular, one of the Pythagorean means. It is sometimes appropriate for situations when the average rate is desired.

**Example:**
```py
import pythmath

data = [6, 7, 3, 9, 10, 15]

print(pythmath.harmonic_mean(data))
```
**Output:** 6.517241379310345

## Geometric Mean:
It is a function that calculates the geometric mean from given dataset, list of numbers or tuple of numbers.

**Geometric Mean:** In statistics, the geometric mean is calculated by raising the product of a series of numbers to the inverse of the total length of the series. The geometric mean is most useful when numbers in the series are not independent of each other or if numbers tend to make large fluctuations.

**Example:**
```py
import pythmath

data = [1, 2, 3, 4, 5]

print(pythmath.geometric_mean(data))
```
**Output:** 2.605171084697352

## Median Absolute Deviation:
It is a function that calculates the median absolute deviation from a given dataset, list of numbers or tuple of numbers.

**Median Absolute Deviation:** In statistics, the median absolute deviation is a robust measure of the variability of a univariate sample of quantitative data. It can also refer to the population parameter that is estimated by the MAD calculated from a sample.

**Example:**
```py
import pythmath

data = [1, 2, 3, 4, 5]

print(pythmath.median_abs_dev([1, 2, 3, 4, 5]))
```
**Output:** 1.0

## Covariance:
It is a function that calculates the covariance from two datasets or lists of numbers x and y. It takes three parameters: **x: values of dataset x**, **y: values of dataset y** and **cov_mode: mode of covariance either sample(samp) or population(pop), by default it is sample**

**Covariance:** In probability theory and statistics, covariance is a measure of the joint variability of two random variables. If the greater values of one variable mainly correspond with the greater values of the other variable, and the same holds for the lesser values, the covariance is positive.

**Example:**

**With cov_mode=samp**
```py
import pythmath

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(pythmath.covariance(x, y, cov_mode="samp"))
```
**Output:** 1.6666666666666667

**With cov_mode=pop**
```py
import pythmath

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(pythmath.covariance(x, y, cov_mode="pop"))
```
**Output:** 1.25

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

## Array Sum:
It is a function that calculates the sum of numbers in a **1d Array**.

**Example:**
```py
import pythmath

array = {12, 3, 4, 15}

print(pythmath.arr_sum(array))
```
**Output:** 34

## Array 2d Sum:
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

## nCr:
It is a function that calculates the Combinations nCr from n a r values.

**Example:**
```py
import pythmath

n = 10
r = 5

print(pythmath.nCr(n, r))
```
**Output:** 252.0

## nPr:
It is a function that calculates Permutations nPr from n and r values.

**Example:**
```py
import pythmath

n = 5
r = 2

print(pythmath.nCr(n, r))
```
**Output:** 20.0

## Fibonacci Series:
It is a function that generates the fibonacci series from n_terms. It takes three parameters **first**, **second** and **n_terms**.
**n_terms:** Number of terms to generate fibonacci series, by default its value is **5** and it is optional. If you leave it by default it generates fibonacci series to **5 terms**.

**Example:**
```py
import pythmath

print(pythmath.fibonacci(0, 2))
```
**Output:** [0, 2, 2, 4, 6]

## Multiply Two List:
It is a function that multiplies each number in two list **List 1** and **List 2** and returns a new multiplied list of these numbers.

**Example:**
```py
import pythmath

x = [1, 2, 3, 4]
y = [5, 2, 4, 1]

print(pythmath.mult_two_lst(x, y))
```
**Output:** [5, 4, 12, 4]

## Square of Two List:
It is a function that squares each number in a list and returns a new squared list of these numbers.

**Example:**
```py
import pythmath

x = [1, 2, 3, 4]

print(pythmath.square_lst(x))
```
**Output:** [1, 4, 9, 16]

## Powered List:
It is a function that calculates the power of each number in a list and returns a new powered list of these numbers. It takes two parameters: **lst: List** and **pow_val**
**pow_val:** Value of power to calculate the power of each number in a list, it is optional and by default its value is 2.

**Example:** 
```py
import pythmath

x = [1, 2, 3, 4]

print(pythmath.pow_lst(x, 3))
```
**Output:** [1, 8, 27, 64]

## Sort List:
It is function that sorts the elements in a list in ascending order. If the list is sorted it will print the message: **The list is already sorted!**

**Example:**
```py
import pythmath

my_list = [5, 10, 4, 3, 2, 17]
lst = [1, 2, 3, 4, 5]

print(pythmath.sort(my_list))
print(pythmath.sort(lst))
```
**Output of my_list:** [2, 3, 4, 5, 10, 17]

**Output of lst:** The list is already sorted!

## Count List:
It is a function that counts how many numbers in a list.

**Example:**
```py
import pythmath

results = [1, 2, 3, 4, 5]

print(pythmath.count(results))
```
**Output:** 5

## Minimum in List:
It is a function that finds the minimum value in a list.

**Example:**
```py
import pythmath

lst = [1, 2, 3, 4, 5]

print(pythmath.minimum(lst))
```
**Output:** 1

## Maximum in a List:
It is a function that finds the maximum value in a list.

**Example:**
```py
import pythmath

lst = [1, 2, 3, 4, 5]

print(pythmath.maximum(lst))
```
**Output:** 5

## Is Float:
It is a function that checks whether the number is float or not and returns True if the number is float otherwise False.

```py
import pythmath

num1 = 7.5
num2 = 7

print(pythmath.isfloat(num1))
print(pythmath.isfloat(num2))
```
**Output of num1:** True
**Output of num2:** False

## Positive or Negative Number:
It is a function that returns the positive number if the inputted number is negative and returns negative number if the inputted number is positive.

```py
import pythmath

num1 = -7
num2 = 7
num3 = 7.5
num4 = -7.5

print(pythmath.pos_neg(num1))
print(pythmath.pos_neg(num2))
print(pythmath.pos_neg(num3))
print(pythmath.pos_neg(num4))
```
**Output of num1:** 7

**Output of num2:** -7

**Output of num3:** -7.5

**Output of num4:** 7.5

For more basic math functions see [Examples/Basic Math Functions](https://github.com/roshaan55/pythmath/tree/main/Examples/Basic%20Math%20Funcions "Examples of basic math functions").

# Area Functions:
## Area of Rectangle Function:
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

# Trignometric Functions:
## Sin(x) Function:
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

# Statistical Functions:
## Mean:
It is a function to calculate the mean of given dataset or list.
**Mean:** In mathematics and statistics, the arithmetic mean or arithmetic average, or simply just the mean or the average, is the sum of a collection of numbers divided by the count of numbers in the collection.

**Example:**
```py
import pythmath

numbers = [1, 2, 3, 4, 5]

print(pythmath.mean(numbers))
```
**Output:** 3.0

## Median:
It is function that calculates median of given dataset or list.
**Median:** In statistics and probability theory, the median is the value separating the higher half from the lower half of a data sample, a population, or a probability distribution. For a data set, it may be thought of as "the middle" value.

**Example:**
```py
import pythmath

numbers = [1, 2, 3, 4, 5]

print(pythmath.median(numbers))
```
**Output:** 3

## Mode:
It is a function that gets the mode of given datasets or list.
**Mode:** The mode is the value that appears most often in a set of data values. If X is a discrete random variable, the mode is the value x at which the probability mass function takes its maximum value. In other words, it is the value that is most likely to be sampled.

**Example:**
```py
import pythmath

numbers = [1, 2, 3, 4, 5, 5]

print(pythmath.mode(numbers))
```
**Output:** 5

## Standard Deviation:
It calculates the standard deviation from given dataset or list of numbers.
**Standard Deviation:** In statistics, the standard deviation is a measure of the amount of variation or dispersion of a set of values. A low standard deviation indicates that the values tend to be close to the mean of the set, while a high standard deviation indicates that the values are spread out over a wider range.

**Example:**
```py
import pythmath

data = [1, 2, 3, 4, 5]

print(pythmath.stdev(data))
```
**Output:** 1.5811388300841898

## Population Standard Deviation:
It is a function that calculates population standard deviation from given dataset or list of numbers.

**Example:**
```py
import pythmath

data = [1, 2, 3, 4, 5]

print(pythmath.pstdev(data))
```
**Output:** 1.4142135623730951

## Mean Absolute Deviation(MAD):
It is a function that calculates the mean absolute deviation from given dataset or list of numbers.
**Mean Absolute Deviation:** The mean absolute deviation (MAD) is a measure of variability that indicates the average distance between observations and their mean. MAD uses the original units of the data, which simplifies interpretation. Larger values signify that the data points spread out further from the average. Conversely, lower values correspond to data points bunching closer to it. The mean absolute deviation is also known as the mean deviation and average absolute deviation.

**Example:**
```py
import pythmath

data = [1, 2, 3, 4, 5]

print(pythmath.mean_abs_dev(data))
```
**Output:** 1.2

## Variance:
It is a function that calculates the variance from given dataset or list of values. it takes two parameters: **data: values of dataset** and **v_mode**.
**v_mode:** Mode of variance either standard(std) or population(pop), it is optional and by default its mode is standard(std)
**Note:** pop does not equivalent to stack pop.

**Example:**

**With v_mode="std"**
```py
import pythmath

data = [2, 4, 6, 8, 10]

print(pythmath.variance(data))
```
**Output:** 10.0

**With v_mode="pop"**
```py
import pythmath

data = [2, 4, 6, 8, 10]

print(pythmath.variance(data, v_mode="pop"))
```
**Output:** 8.0

## Z Score:
It is a function that calculates the z score value from x, mean value and from value of standard deviation.
**Z Score:** In statistics, the standard score is the number of standard deviations by which the value of a raw score is above or below the mean value of what is being observed or measured. Raw scores above the mean have positive standard scores, while those below the mean have negative standard scores.

**Example:**
```py
import pythmath

x = 70
mean_val = 60
st_dev = 15

print(pythmath.zscore(x, mean_val, st_dev))
```
**Output:** 0.6666666666666666

## Standard Error:
It is a function that calculates standard error from given dataset or from list of numbers.
**Standard Error:** The standard error of a statistic is the standard deviation of its sampling distribution or an estimate of that standard deviation. If the statistic is the sample mean, it is called the standard error of the mean.

**Example:**
```py
import pythmath

data = [10, 12, 16, 21, 25]

print(pythmath.stderr(data))
```
**Output:** 2.782085548648711

## Sampling Error:
It is a function that calculates the sampling error. It takes three parameters: **n**, **pst_dev** and **conf**
**n:** Size of sampling.
**pst_dev:** Population Standard Deviation
**conf:** Confidence level approx 1.96, it is optional and by default its value is set 1.96

**Example:**
```py
import pythmath

n = 2500
pst_dev = 0.40

print(pythmath.samp_err(n, pst_dev))
```
**Output:** 0.01568

## Statistical Range:
It is a function that calculates the statistical range from given dataset or set of integer values.
**Statistical Range:** In statistics, the range of a set of data is the difference between the largest and smallest values. Difference here is specific, the range of a set of data is the result of subtracting the sample maximum and minimum. However, in descriptive statistics, this concept of range has a more complex meaning.

**Example:**
```py
import pythmath

lst = [1, 2, 3, 4, 5]

print(pythmath.stats_range(lst))
```
**Output:** 4

## Mid Range:
It is a function that calculates the midpoint range from given dataset or set of integer values.
**Mid Range:** In statistics, the mid-range or mid-extreme is a measure of central tendency of a sample defined as the arithmetic mean of the maximum and minimum values of the data set.

**Example:**
```py
import pythmath

lst = [1, 2, 3, 4, 5]

print(pythmath.midrange(lst))
```
**Output:** 3.0

# Error Functions:
## Percentage Error:
It is a funcion that calculates the percentage error from measured value and true or real value.

**Example:**
```py
import pythmath

measured_val = 8
true_val = 10

print(pythmath.perc_err(measured_val, true_val))
```
**Output:** 20.0

## Absolute Error:
It is a function that calculates the absolute error from measured value and true or real value.

**Example:**
```py
import pythmath

measured_val = 8
true_val = 10

print(pythmath.abs_err(measured_val, true_val))
```
**Output:** 2

## Relatable Error:
It is a function that calculates the relatable error from measured value and true or real value.

**Example:**
```py
import pythmath

measured_val = 8
true_val = 10

print(pythmath.rel_error(measured_val, true_val))
```
**Output:** 0.2

For more examples see [Examples](https://github.com/roshaan55/pythmath/blob/main/Examples "Examples of funcions of pythmath").


