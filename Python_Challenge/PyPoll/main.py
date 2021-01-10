# Import required modules
import os # Used to create file paths across operating systems
import csv # Used for reading CSV files

# Identify file path
election_path = os.path.join('Resources','election_data.csv')

# Read from the csv file
with open(election_path,'rt') as election_file:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(election_file, delimiter=',')

    # Read headers into a variable for reference while coding
    election_header = next(csvreader)
    print(f"Header: {election_header}")

    # Create dictionary
    election_dict = {}

    for row in csvreader:
        # Read csv into dctionary
        election_dict[row[0]] = {election_header[1]: row[1], election_header[2]: row[2]}

    total_votes = 0
    winner_name = 'TBD'

    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote

# Build output text
output_text = 'Election Results'+'\n'
output_text = output_text+F'----------------------------------------------------'+'\n'
output_text = output_text+F'Total Votes: {total_votes}'+'\n'
output_text = output_text+F'----------------------------------------------------'+'\n'
# Insert list of candidates & vote percentage
output_text = output_text+F'----------------------------------------------------'+'\n'
output_text = output_text+F'Winner: {winner_name}'+'\n'
output_text = output_text+F'----------------------------------------------------'+'\n'

# Print output to terminal
print(output_text)

# Write output to text file
output_path = os.path.join('Analysis','election_analysis.txt')
output_file = open(output_path,'wt')
output_file.write(output_text)
