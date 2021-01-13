# Import required modules
import os # Used to create file paths across operating systems
import csv # Used for reading CSV files

# Identify file path
election_path = os.path.join('Resources','election_data.csv')

# Read from the csv file
with open(election_path,'rt') as election_file:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(election_file, delimiter=',')

    # Read headers into a variable
    election_header = next(csvreader)
    #print(f"Header: {election_header}")

    # Create dictionary
    results_dict = {}

    for row in csvreader:
        # If candidate is in dictionary, incriment vote count by 1.
        if row[2] in results_dict.keys():
           results_dict[row[2]]["Votes"] += 1
        # If the candidate is not in dictionary, add it and set votes to 1
        else:
            results_dict[row[2]] = {"Votes":1}
    
    #close csv file
    election_file.close()

# The total number of votes cast
total_votes = sum([results_dict[row]["Votes"] for row in results_dict])


# A complete list of candidates who received votes, their percentage of votes, & their total votes
candidates = ''
for row in results_dict:
    percent_votes = "{:3.3f}".format(results_dict[row]["Votes"] /total_votes * 100)
    candidates += f'{row}: {percent_votes}% ({results_dict[row]["Votes"]})\n'

# The winner of the election based on popular vote
max_votes = max([results_dict[row]["Votes"] for row in results_dict])
winner_name = [row for row in results_dict if results_dict[row]["Votes"] == max_votes][0]

# Build output text
output_text = 'Election Results\n'
output_text = output_text+F'----------------------------------------------------\n'
output_text = output_text+F'Total Votes: {total_votes}\n'
output_text = output_text+F'----------------------------------------------------\n'
output_text = output_text+candidates
output_text = output_text+F'----------------------------------------------------\n'
output_text = output_text+F'Winner: {winner_name}\n'
output_text = output_text+F'----------------------------------------------------'

# Print output to terminal
print(output_text)

# Write output to text file & close csv file
output_path = os.path.join('Analysis','election_analysis.txt')
output_file = open(output_path,'wt')
output_file.write(output_text)
output_file.close()