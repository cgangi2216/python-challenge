# Import required modules
import os # Used to create file paths across operating systems
import csv # Used for reading CSV files

# Identify file path
budget_path = os.path.join('Resources','budget_data.csv')

# Read from the csv file
with open(budget_path,'rt') as budget_file:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget_file, delimiter=',')

    # Read headers into a variable
    budget_header = next(csvreader)
    #print(f"Header: {budget_header}")

    # Create dictionary
    budget_dict = {}

    # Create variables for calculating change in Profit/Losses
    row_ct = 1
    profit_loss_previous = 0

    # Read csv into dictionary & calculate change in Profit/Losses
    for row in csvreader:
        # If this is the 1st row, skip it. If not, compare Profit/Losses to last month.
        if row_ct == 1:
            profit_loss_change = None
        else:
            profit_loss_change = int(row[1]) - int(profit_loss_previous)

        budget_dict[row[0]] = {budget_header[1]: int(row[1]), "Change": profit_loss_change}
        
        # Set previous Profit/Losses variable for calculation in next row
        profit_loss_previous = row[1]
        
        # Increment row count variable
        row_ct += 1

    #close csv file
    budget_file.close()

#print(budget_dict)

# Calculate the total number of months included in the dataset
total_months = len(budget_dict)

# Calculate the net total amount of "Profit/Losses" over the entire period
total_profit_losses = sum([budget_dict[row]["Profit/Losses"] for row in budget_dict])

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
avg_change = round(sum([budget_dict[row]["Change"] for row in budget_dict if budget_dict[row]["Change"] != None])/(total_months-1),2)

# Find the greatest increase in profits (date and amount) over the entire period
greatests_increase = max([budget_dict[row]["Change"] for row in budget_dict if budget_dict[row]["Change"] != None])
greatests_increase_month = [row for row in budget_dict if budget_dict[row]["Change"] == greatests_increase][0]

# Find the greatest decrease in losses (date and amount) over the entire period
greatests_decrease = min([budget_dict[row]["Change"] for row in budget_dict if budget_dict[row]["Change"] != None])
greatests_decrease_month = [row for row in budget_dict if budget_dict[row]["Change"] == greatests_decrease][0]
    
# Build output text
output_text = 'Financial Analysis\n'
output_text = output_text+F'----------------------------------------------------\n'
output_text = output_text+F'Total Months: {total_months}\n'
output_text = output_text+F'Total Profit/Losses: ${total_profit_losses}\n'
output_text = output_text+F'Average Change in Profits: ${avg_change}\n'
output_text = output_text+F'Greatest Increase in Profits: {greatests_increase_month} (${greatests_increase})\n'
output_text = output_text+F'Greatest Decrease in Profits: {greatests_decrease_month} (${greatests_decrease})\n'

# Print output to terminal
print(output_text)

# Write output to text file & close csv file
output_path = os.path.join('Analysis','budget_analysis.txt')
output_file = open(output_path,'wt')
output_file.write(output_text)
output_file.close()