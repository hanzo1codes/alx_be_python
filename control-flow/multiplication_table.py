def print_multiplication_table():
    # Prompt the user for a number
    number = int(input("Enter a number to see its multiplication table: ").strip())

    # Generate and print the multiplication table
    for i in range(1, 10 + 1):
        print(f"{number} * {i} = {number * i}")


# Call the function to execute the script
if __name__ == "__main__":
    print_multiplication_table()
