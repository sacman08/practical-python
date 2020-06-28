# pcost.py
#
# Exercise 1.27
#Write a program called pcost.py that 
#opens this file,
#reads all lines, and 
#calculates how much it cost to purchase all of the shares in the portfolio.
#TODO Sloppy add in last line. Correct with for loop to look for int and float to total

import csv

filename = "Data/portfolio.csv"

def portfolio_cost(filename):

    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
            
#print(records)
print("Total share cost:", portfolio_cost(filename))
        