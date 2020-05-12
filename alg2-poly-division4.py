# PROBLEM:
#   Select all polynomials that have (x - 2) as a factor.

# STEP 1: Define polynomials as their own "functions"
def A(x):
    return x**3 + x**2 + 4

def B(x):
    return x**3 - x - 6

def C(x):
    return x**4 + 3*x - 10

def D(x):
    return x**4 - 2*(x**3) - 2


# STEP 2: test each polynomial against 2 (we're using remainder theorum)
polynomials = [A,B,C,D]
for P in polynomials:
    if (P(2) == 0):
        print(P)

# STEP 3:
# result = <function B at 0x7fd6888d9620> 

# B is the answer
