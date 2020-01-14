# Import the data and skip headers
import csv
with open(PyPoll_Resources_election_data) as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader, None)
    headers['Voter ID', 'County', 'Candidate']

#Tally total votes cast
total_votes = sum(1 for row in csvfile)

# Print total votes cast
print(f'Total Votes: {total_votes}')

# List candidates who received votes
df=pd.read_csv('PyPoll_Resources_election_data',header=1)
df.apply(set)

# Calculate number of votes per candidate

# Print each candidate's name and number of votes

# Find candidate with maximum number of votes

# Print winning candiate's name
