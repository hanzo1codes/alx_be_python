income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

# to customize it so you add your interest rate
interest_rate = (input("Enter your interest rate: "))
actual_interest_rate = float(interest_rate.strip('%')) / int(100)

# to calculate your monthly savings
savings = income - expenses
print(f"Your monthly savings are ${savings}.")

# to calculate your annual savings with interest
annual_savings = (savings * 12) + (savings * 12 * actual_interest_rate)
# annual_savings = (savings * 12) + (savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${annual_savings}")