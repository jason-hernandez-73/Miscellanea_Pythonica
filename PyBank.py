# Import the file and get past the headers
import csv
with open(PyBank_Resources_budget_data) as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader, None)
    headers['Date', 'Profit/Losses']
    
# Count the number of months
total_months = sum(1 for row in csvfile)

# Ticker the profits and losses
total_profits_losses = sum(int(row[1]) for row in csvfile)

# Average the changes in profits and losses
change = next(cr)
    for row in cr:
        change = [x - y for x, y in zip(change, row)]
average_change = [x / n for n in change]
        