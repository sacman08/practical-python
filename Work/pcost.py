# pcost.py
#
# Exercise 1.27
#Write a program called pcost.py that 
#opens this file,
#reads all lines, and 
#calculates how much it cost to purchase all of the shares in the portfolio.
#TODO Sloppy add in last line. Correct with for loop to look for int and float to total

filename = 'Data/portfolio.csv'
records = []
totals = []
with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        records.append(row[0])
        records.append(int(row[1]) * float(row[2]))
        
    for x in records:
        if records[x].is_integer:
            if records[x+1].is_float:
                totals = records[x] * records[x+1]
            else:
                break
            
#print(records)
print('Total cost for all shares:', totals)
        