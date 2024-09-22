
# DSC 510
# Week 2 Programming Assignment 3.2
# Author Sherrell Bacon
# 9/11/2024

#Change Control Log:
#Change#:1
#Changes Made: Added error handling to check for invalid input lines 23-29,
#added updated price per foot calculation
#Date of Change: 9/11/2024
#Author: Sherrell Bacon
#Change Approved by: Prof. Eller
#Date Moved to Production: 9/14/2024
# -------------------------------------------------------------
# Display welcome message to the user
print("Welcome to the Fiber Optic Cable Installation Calculator.")

# Obtain the company name from user
company_name = input("Please enter your company name: ")

#Retrieve the number of feet of fiber optic cable to be installed from the user.
cable_feet = input("Please enter the number feet of cable do you need: ")
try:
    cable_feet = float(cable_feet)
#Determine the price per foot
    if cable_feet >500:
        cost_per_foot = 0.50
    elif cable_feet >250:
        cost_per_foot = 0.70
    elif cable_feet >100:
        cost_per_foot = 0.80
    else:
        cost_per_foot = 0.87
#Calculate the installation cost
    total_cost = cable_feet * cost_per_foot
# Print a receipt for the user
    print("----Installation Receipt----")
    print("Company Name:", company_name)
    print("Fiber Optic Cable Feet Requested:", cable_feet)
    print("Cost Per Foot $", cost_per_foot)
    print("Total Installation Cost $", total_cost)
    print("-----------------------------")
#If the input is invalid (not a number), handle the error
except TypeError:
    print("Please enter a valid number.")
except ValueError:
    print("Please enter a valid number.")