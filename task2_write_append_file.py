# Task 2: Write and Append Data to a File

# Step 1: Take user input and write it to output.txt
user_input = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Initial data written to 'output.txt'.")

# Step 2: Append additional data to the same file
additional_input = input("Enter additional text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

print("Additional data appended to 'output.txt'.")

# Step 3: Read and display the final content of the file
print("\nFinal content of 'output.txt':\n")

with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
