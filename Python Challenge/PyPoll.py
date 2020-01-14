# Import the data and skip headers
import os
import csv
election_data_csv = os.path.join("..", "UC-Berkeley", "Python Challenge", "PyPoll_Resources_election_data.csv")

with open(PyPoll_Resources_election_data) as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader, None)
    headers['Voter ID', 'County', 'Candidate']

#Tally total votes cast
total_votes = sum(1 for row in csvfile)

# Print total votes cast
print("Election Results")
print("-") * 20
print(f'Total Votes: {total_votes}')
print("-") * 20

# List candidates who received votes
# function to get unique values 
def unique(csvfile): 
  
    # intilize a null list 
    unique_names = [] 
      
    # check for all elements in "Candidate" column
    for x in csvfile: 
        # check if exists in unique_list or not 
        if x not in unique_names: 
            unique_names.append(x) 

# Calculate number of votes per candidate
with open(PyPoll_Resources_election_data), newline='') as f:
    reader = csv.reader(f)
    vote_counts = Counter(map(itemgetter(2), reader))
    percent_votes = (vote_counts / total_votes)

# Print each candidate's name and number of votes
print(f {unique_names},": ", {percent_votes}, {vote_counts})

# Find candidate with maximum number of votes
winner = max(vote_counts)

# Print winning candiate's name
print("-") * 20
print("Winner: ", )
print("-") * 20