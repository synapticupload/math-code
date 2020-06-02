# QUESTION: What is the limit of (x**5 - 3*x + 4)**3 as x approaches 2? 
# ------------------------------------------------------------------------------

# CODE/NOTES
# --------------------------------------

# The limit of a polynomial,
#     as x approaches number a, is 
#     found by evaluating the polynomial
#     for the number a.

# We'll start by defining a function for the polynomial in the question.
# It simply returns the y value when supplied the x value.

def p1(x):                              # p1 = "polyomial 1"
    return ((x**5) - (3*x) + 4)**3

x1 = 2                                  # x coordinate 1 will have a value of 2
l1 = p1(x1)                             # limit 1 will be result of p1(x1)
print(l1)                               # print the value

# ANSWER
# --------------------------------------
# 27,000
