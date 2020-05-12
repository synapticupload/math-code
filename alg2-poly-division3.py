# PROBLEM:
# ------------------------------------------------------------------------------
# 
#     Which polynomials have (x - 3) as a factor?
#     **NOTE: I've defined them below instead of here.
#
# SOLUTION:
# ------------------------------------------------------------------------------
#
# First, let's define our polynomials as their own functions.
# ----------------------------------------------------------

def A(x):
    return x**3 - 2*(x**2) - 4*x + 3

def B(x):
    return x**3 + 3*(x**2) - 2*x - 6

def C(x):
    return x**4 - 2*(x**3) - 27

def D(x):
    return x**4 - 20*x - 21

# ----------------------------------------------------------
# So I've defined all of my polynomials, now I need to find which ones...
#     ... have (x - 3) as a factor.
#
# Using the polynomial remainder theorum, if dividing by (x - a), then...
#     ... P(a) will result in the remainder. 
#
# In our case, we need to evaluate P(3). If the remainder is 0, then...
#     ... we know our divisor is indeed a factor.
# ----------------------------------------------------------

a = 3

# ----------------------------------------------------------
# APPROACH 1:
#     We can store all of our polynomials in a list
# ----------------------------------------------------------

polynomial_list = [A, B, C, D]

# ----------------------------------------------------------
#     And then we can evaluate each one for a, which is 3
# ----------------------------------------------------------

for polynomial in polynomial_list:
    if (polynomial(a) == 0):
        print(polynomial)

# ----------------------------------------------------------
# this results in:
#   <function A at 0x7f741b3a1e18>
#   <function C at 0x7f741b1d98c8>
#   <function D at 0x7f741b1d9950>
#
# So we know that functions (or polynomials) A, C, D have a factor of (x - 3)
# ----------------------------------------------------------
