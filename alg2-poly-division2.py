# PROBLEM:
# ------------------------------------------------------------------------------
# 
#     P(x) = x^3 + 2x^2 + cx + 10
# 
#     For what c is (x - 5) a factor of P?
# 
#
# SOLUTION:
# ------------------------------------------------------------------------------

# We'll start by defining the polynomial as its own function
def P(x, c):
    return x**3 + 2*(x**2) + c*x + 10

# We'll then take advantage of the polynomial remainder theorum.
# When dividing by (x - a), P(a) will simply be the remainder.
# So we'll plug in P(5, c) but we need to test for c

# One way is to brute force...
for i in range(-100000, 100000):
    if (P(5, i) == 0):
        print("The value of c is " + str(i))

# c would be -37, computed in under 1 second
