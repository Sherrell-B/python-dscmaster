
# DSC 510
# Week 2 Programming Assignment 2.1
# Author Sherrell Bacon
# 9/1/2024
# -------------------------------------------------------------

# Display welcome message to the user
print("Welcome to the Fiber Optic Cable Installation Calculator.")

# Obtain the company name from user
company_name = input("Please enter your company name: ")

#Retrieve the number of feet of fiber optic cable to be installed from the user.
cable_feet = float(input("Please enter the number feet of cable do you need: "))

#Calculate the installation cost
cost_per_foot = 0.87
total_cost = cable_feet * cost_per_foot

# Print a receipt for the user
print ("---Installation Receipt---")
print("Company Name:", company_name)
print("Feet of Fiber Optic Cable:", cable_feet)
print("Cost Per Foot", cost_per_foot)
print("Total Installation Cost", total_cost)