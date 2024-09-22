# Display a welcome message for the user
print("Welcome to the Fiber Optic Cable Installation Cost Calculator!")

# Retrieve the company name from the user
company_name = input("Please enter your company name: ")

# Retrieve the number of feet of fiber optic cable to be installed from the user
try:
    num_feet = float(input("Please enter the number of feet of fiber optic cable to be installed: "))
    if num_feet < 0:
        raise ValueError("The number of feet cannot be negative.")  # Check for invalid input
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

# Calculate the installation cost (0.87 per foot)
cost_per_foot = 0.87
total_cost = num_feet * cost_per_foot

# Print a receipt for the user
print("\n--- Installation Receipt ---")
print(f"Company Name: {company_name}")
print(f"Feet of Fiber Optic Cable: {num_feet:.2f}")
print(f"Cost per Foot: ${cost_per_foot:.2f}")
print(f"Total Installation Cost: ${total_cost:.2f}")
print("-----------------------------")

# End of program