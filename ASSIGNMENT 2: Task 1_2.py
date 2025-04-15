# Task 1: Check if a Number is Even or Odd

# Enter a Number
number = int(input("Enter a Number: "))

# Check if number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")



print('\n')


# Task 2: Sum of number from 1 to 50 Using a Loop

# Initialize sum variable
total = 0

# Iterate through numbers 1 to 50 and add to sum
for number in range(1, 51):
    total += number

# Display the result
print(f"The sum of integers from 1 to 50 is: {total}")