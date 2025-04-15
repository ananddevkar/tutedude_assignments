
# Task 1: Read a File and Handle Errors

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"Contents of '{filename}':\n")
            for line in file:
                print(line, end='')  # end='' prevents extra newlines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Call the function
read_file("sample.txt")


print('\n')

# Task 2: Write and Append Data to a File

# Step 1: Write initial data to file
initial_data = input("Enter initial text to write to file: ")
with open("output.txt", "w") as file:
    file.write(initial_data + "\n")  # \n adds a newline

# Step 2: Append additional data
append_data = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_data + "\n")

# Step 3: Read and display final content
print("\nFinal file contents:")
with open("output.txt", "r") as file:
    print(file.read())