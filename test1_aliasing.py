import copy

# Original list
A = [1, 2, 3]

# Aliasing: B points to the same list as A
B = A

# Modifying B will also affect A
B[0] = 10

print("A:", A)
print("B:", B)

# Creating a shallow copy using copy.copy()
B = copy.copy(A)

# Modifying B now won't affect A
B[0] = 100

print("A:", A)
print("B:", B)
