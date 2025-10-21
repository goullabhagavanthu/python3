def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Create closures
times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

# Use the closures
print(times3(9))
print(times5(3))

# Nested Function:
# A closure is always an inner function defined within another function.