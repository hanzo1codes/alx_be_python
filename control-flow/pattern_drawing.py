# pattern_drawing.py

def draw_square_pattern():
    # Prompt the user for a positive integer
    size = int(input("Enter the size of the pattern: ").strip())

    # Ensure the size is positive
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Initialize the row counter
    row = 0

    # Use a while loop to iterate through each row of the pattern
    while row < size:
        # Use a for loop to print asterisks in the current row
        for _ in range(size):
            print("*", end="")
        # Move to the next line after completing the row
        print()
        # Increment the row counter
        row += 1

# Call the function to execute the script
if __name__ == "__main__":
    draw_square_pattern()
