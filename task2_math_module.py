# Task 2: Using the Math Module for Calculations

import math  # Step 1: Import the math module

# Step 2: Take a number as input from the user
number = float(input("Enter a number: "))

# Step 3: Perform calculations using math module
if number > 0:
    sqrt_result = math.sqrt(number)
    log_result = math.log(number)  # Natural logarithm (base e)
else:
    sqrt_result = "Undefined (cannot take sqrt of negative number)"
    log_result = "Undefined (log not defined for 0 or negative numbers)"

sine_result = math.sin(number)  # Sine of the number in radians

# Step 4: Display the results
print("\nCalculated Results:")
print(f"Square Root: {sqrt_result}")
print(f"Natural Logarithm (ln): {log_result}")
print(f"Sine (in radians): {sine_result}")
