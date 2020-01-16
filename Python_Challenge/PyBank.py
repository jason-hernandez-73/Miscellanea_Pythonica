# Import the file and get past the headers
import os
import csv
budget_data_csv = ("PyBank_Resources_budget_data.csv")

# Set initial values
greatest_month_increase = ""
greatest_month_decrease = ""
total_months = 1
total_profits_losses = 0
greatest_increase = -1000000
greatest_decrease = 1000000
changes = []

with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    budget_header = next(csvfile)
    
    # Count the number of months
    previous_row = next(csvreader)
    total_profits_losses = int(previous_row[1])
    for row in csvreader:
        total_months = total_months + 1

    # Ticker the profits and losses
        total_profits_losses = total_profits_losses + int(row[1])

    # Average the changes in profits and losses
        change = int(row[1]) - int(previous_row[1])
        changes.append(change)
        previous_row = row

    # Find the maximum and minimum change
        if change > greatest_increase:
            greatest_increase = change
            greatest_month_increase = row[0]
        elif change < greatest_decrease:
            greatest_decrease = change
            greatest_month_decrease = row[0]

    average_change = total_profits_losses / total_months
    
    # Print the number of months
    print(f'Total Months: {total_months}')

    # Print the net profits/losses
    print(f'Total: ${total_profits_losses}')

    # Print the average change
    print(f'Average Change: {average_change}')

# Print the maximum and minimum change
print(f'Greatest Increase in Profits: {greatest_increase}')
print(f'Greatest Decrease in Profits: {greatest_decrease}')

# Export results to text file
with open("profitLoss.txt","w") as file:
    file.write(
        f'Total Months: {total_months}\n'  
        f'Total: ${total_profits_losses}\n' 
        f'Average Change: {average_change}\n' 
        f'Greatest Increase in Profits: {greatest_month_increase}, {greatest_increase}\n' 
        f'Greatest Decrease in Profits: {greatest_month_decrease}, {greatest_decrease}'
    )
file.close()