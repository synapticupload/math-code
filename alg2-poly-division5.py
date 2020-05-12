# Find the value of "c" so that the polynomial is divisible by (x - 3)
# P(x) = -x**3 + c*(x**2) - 4*x + 3

# Using the remainder theorum, we'll plug in a, which is 3
x = 3

def P(x, c):
    return -1*(x**3) + c*(x**2) - 4*x + 3

for i in range(-1000000, 1000000):
    if (P(x, i) == 0):
        print(i)
