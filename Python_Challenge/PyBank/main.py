# Used to create file paths across operating systems
import os

# Used for reading CSV files
import csv

# Identify file path
budget_path = os.path.join('Resources','budget_data.csv')

# Read from the csv file
with open(budget_path,'rt') as budget_file:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_file, delimiter=',')

    # Read headers into a variable for reference while coding
    budget_header = next(csvreader)
    # print(f"Header: {budget_header}")

    # Create list of 
    profit_loss = [int(row[1]) for row in csvreader]
    
    # Count months in file
    total_months = len(profit_loss)
    
    # Total Profit/Losses
    total_profit_loss = sum(profit_loss)

    # Average Change in Profit/Losses




    # Greatest Increase in Profit/Losses
    # Greatest Decrease in Profit/Losses
    
    # Print output to terminal
    print('----------------------------------------------------')
    print('Financial Analysis')
    print('----------------------------------------------------')
    print(F'Total Months: {total_months}')
    print(F'Total Profit/Losses: ${total_profit_loss}')

    # Write output to text file









