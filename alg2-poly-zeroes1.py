# The following polynomial is factored:
def P(x):
    return (x - 1)*(x + 2)*(x - 3)*(x + 4)

# Find the zeroes of the polynomial
for x in range(-10, 10):
    if (P(x) == 0):
        print(x)

# print them as coordinate pairs
for x in range(-10, 10):
    y = (P(x))
    if (y == 0):
        coord = (x, y)      # I chose to use tuples
        print(coord)
