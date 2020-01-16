# Import the data and skip headers
import os
import csv
election_data_csv = ("PyPoll_Resources_election_data.csv")

# Set initial values
total_votes = 0
vote_counts_dict = {"Candidate": {}, "Votes": {}}
percent_votes = 0
name = []
unique_names = [] 
winner = ""

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader, None)

    for name in csvfile: 
        #Tally total votes cast
        total_votes = total_votes + 1

        # List candidates who received votes
        name = str(election_data_csv[2])

        # check for all elements in "Candidate" column
            # check if exists in unique list or not 
        if name not in unique_names: 
            unique_names.append(name)
            vote_count = 1
            vote_counts_dict.update({"Candidate" : name , "Votes" : vote_count}) # Code from javatpoint.com
        else: 
            vote_count = vote_count + 1
            vote_counts_dict.update({"Candidate" : name , "Votes" : vote_count})
        percent_votes = (vote_count / total_votes)

# Print total votes cast
print("Election Results")
print("--------------")
print(f'Total Votes: {total_votes}')
print("--------------")

# Print each candidate's name and number of votes
print(f'{unique_names},": ", {percent_votes}, {vote_count}')

# Find candidate with maximum number of votes
winner = max(vote_count)

# Print winning candiate's name
print("--------------")
print(f"Winner: , {winner}, row[2], votes")
print("--------------")