# Global variable
x = 10

def example_function():
    # This will create a local variable x, it doesn't affect the global x
    x = 20
    print(f"Inside function, local x = {x}")

# Call the function
example_function()

# Print the global x
print(f"Outside function, global x = {x}")