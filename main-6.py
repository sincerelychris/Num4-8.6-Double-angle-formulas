#Homework: 8.6 Double angle formulas (Copy
#number 4
# File name :  Screenshot 2024-04-21 at 4.14.00 PM


import math
from sympy import *

# Given value
sin_theta = Rational(6, 7)

# Calculate cos_theta using the Pythagorean identity
cos_theta = sqrt(1 - sin_theta**2)

# Calculate sin(2*theta) using the formula 2*sin(theta)*cos(theta)
sin_2theta = 2*sin_theta*cos_theta

# Simplify the result to get the exact value
exact_value = simplify(sin_2theta)

print(f"The exact value of sin(2*theta) is {exact_value}")


import math
from sympy import *


# Given value
sin_theta = Rational(6, 7)

# Calculate cos_theta using the Pythagorean identity
cos_theta = sqrt(1 - sin_theta**2)

# Calculate cos(2*theta) using the formula cos^2(theta) - sin^2(theta)
cos_2theta = cos_theta**2 - sin_theta**2

# Simplify the result to get the exact value
exact_value = simplify(cos_2theta)

print(f"The exact value of cos(2*theta) is {exact_value}")

