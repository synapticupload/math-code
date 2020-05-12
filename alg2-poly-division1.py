# PROBLEM: 
#
# For polynomial:           
#   P(x) = 2x^4 - 11x^3 + 15x^2 + 4x - 12
#
# Is (x-3) a factor of P?

# SOLUTION: 
#   Use polynomial remainder theorum (so P(a) = remainder, or P(3) = remainder)
#   if remainder == 0, then (x-3) is a factor

# First I've defined the polynomial as a function in Python
def polynomial_P(x):
    return 2*(x**4) - 11*(x**3) + 15*(x**2) + 4*(x) - 12

# Next, using the polynomial remainder theorum, supply the a from (x - a)
result = polynomial_P(3)

# if the result was 0, then (x - 3) is a factor of P
if (result == 0):
    print("(x - 3) is a factor of P")
else
    print("(x - 3) isn't a factor..")
