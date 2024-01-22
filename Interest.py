# Input principal amount, rate of interest, and time period
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in percentage): "))
time_period = float(input("Enter the time period (in years): "))

# Convert rate of interest from percentage to decimal
rate_of_interest_decimal = rate_of_interest / 100

# Calculate simple interest
simple_interest = (principal * rate_of_interest_decimal * time_period)

# Print the calculated simple interest
print(f"The simple interest is: {simple_interest}")
