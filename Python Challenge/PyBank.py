# Import the file and get past the headers
import os
import csv
budget_data_csv = os.path.join("..", "UC-Berkeley", "Python Challenge", PyBank_Resources_budget_data.csv)
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budget_header = next(csvfile)
    budget_header['Date', 'Profit/Losses']
    
# Count the number of months
for row in csvreader:
    total_months = sum(1 for row in csvfile)

# Print the number of months
    print(f'Total Months: {total_months}')

# Ticker the profits and losses
    total_profits_losses = sum(int(row[1]) for row in csvfile)

# Print the net profits/losses
    print(f'Total: ${total_profits_losses}')

# Average the changes in profits and losses
    change = next(cr)
    for row in cr:
        change = [x - y for x, y in zip(change, row)]
    average_change = [x / n for n in change]

# Print the average change
    print(f'Average Change: {average_change}')

# Find the maximum and minimum change
    greatest_increase = max(change)
    greatest_decrease = min(change)

# Print the maximum and minimum change
    print(f'Greatest Increase in Profits: {greatest_increase}')
    print(f'Greatest Decrease in Profits: {greatest_decrease}')

# Export results to text file
f= open("profitLoss.txt","w+")
file.write(
    f'Total Months: {total_months}', 
    f'Total: ${total_profits_losses}', 
    f'Average Change: {average_change}', 
    f'Greatest Increase in Profits: {greatest_increase}', 
    f'Greatest Decrease in Profits: {greatest_decrease}'
)
f.close()