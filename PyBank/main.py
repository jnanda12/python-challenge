import csv
import os

path = 'budget_data.csv'
count = 0
profit_loss = 0
first_month = 0
last_month = 0
monthly_change = 0
sum_change = 0
average_change = 0
max = 0
min = 0
with open(path, 'r', newline='', encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        count = count + 1
        profit_loss = float(row[1]) + profit_loss
        if last_month != 0:
            monthly_change = float(row[1]) - float(last_month)
            sum_change = sum_change + monthly_change
        last_month = row[1]

        if monthly_change > max:
            max = monthly_change
            max_date = row[0]
        if monthly_change < min:
            min = monthly_change
            min_date = row[0]

    average_change = float(sum_change)/float(count-1)
    profit_loss = '{0:.2f}'.format(profit_loss)
    average_change = '{0:.2f}'.format(average_change)
    max = '{0:.2f}'.format(max)
    min = '{0:.2f}'.format(min)

    print('Financial Analysis: ')
    print(f'Total Months: {count}')
    print(f'Total: ${profit_loss}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {max_date} ${max}')
    print(f'Greatest Decrease in Profits: {min_date} ${min}')

file = open('Output.txt', 'w')
file.write('Financial Analysis: ') 
file.write('\nTotal Months: ' + str(count)) 
file.write('\nTotal: $' + str(profit_loss)) 
file.write('\nAverage Change: $' + str(average_change)) 
file.write('\nGreatest Increase in Profits: ' + str(max_date) + ' $' + str(max)) 
file.write('\nGreatest Decrease in Profits: ' + str(min_date) + ' $' + str(min)) 

file.close()
