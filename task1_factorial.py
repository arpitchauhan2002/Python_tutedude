# Task 1: Calculate Factorial Using a Function

# Step 1: Define the factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Step 2 & 3: Call the function with a sample number and display the result
number = int(input("Enter a number to calculate its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(number)
    print(f"The factorial of {number} is: {fact}")
