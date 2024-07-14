def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        demon = float(denominator)
        if demon == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / demon}"
    except ValueError:
        return "Error: Please enter numeric values only."


if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 5))
    print(safe_divide("ten", 5))
