# TASK - 1

def factorial(n):
    """Calculates factorial using a loop"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function
num = int(input('Enter a Number: '))
print(f"The factorial of {num} is: {factorial(num)}")

print('\n')


# TASK - 2
import math

# user input
number = float(input("Enter a number: "))

# Calculate results using math module
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)

# Display results
print(f"\nCalculations for {number}:")
print(f"Square root: {square_root:.4f}")
print(f"Logarithm: {natural_log:.4f}")
print(f"Sine: {sine_value:.4f}")