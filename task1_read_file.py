# Task 1: Read a File and Handle Errors

# Step 1-3: Try reading from the file and handle errors
try:
    with open("sample.txt", "r") as file:
        print("File content:\n")
        for line in file:
            print(line.strip())  # strip() to remove extra newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
