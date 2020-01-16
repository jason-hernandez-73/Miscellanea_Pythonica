# Import the file and get past the headers
import os
import csv
budget_data_csv = os.path.join("..", "PyBank_Resources_budget_data.csv")

# Set initial values
greatest_month_increase = 0
greatrest_month_decrease = 0
total_months = 0
total_profits_losses = 0
greatest_increase = 0
greatest_decrease = 0

with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budget_header = next(csvfile)
    
    # Count the number of months
    row = next(csvreader)
    for row in csvreader:
        previous_row = int(row[1])
        total_months = total_months + 1

    # Ticker the profits and losses
        total_profits_losses = total_profits_losses + int(row[1])

# Average the changes in profits and losses
        change = next(csvreader)
        for row in csvreader:
            change = int(row[1]) - previous_row
            average_change = total_profits_losses / total_months

    # Print the number of months
    print(f'Total Months: {total_months}')

    # Print the net profits/losses
    print(f'Total: ${total_profits_losses}')

    # Print the average change
    print(f'Average Change: {average_change}')

# Find the maximum and minimum change
greatest_increase = max(change)
greatest_decrease = min(change)

# Print the maximum and minimum change
print(f'Greatest Increase in Profits: {greatest_increase}')
print(f'Greatest Decrease in Profits: {greatest_decrease}')

# Export results to text file
f = open("profitLoss.txt","w+")
file.write(
    f'Total Months: {total_months}', 
    f'Total: ${total_profits_losses}', 
    f'Average Change: {average_change}', 
    f'Greatest Increase in Profits: {greatest_increase}', 
    f'Greatest Decrease in Profits: {greatest_decrease}'
)
f.close()