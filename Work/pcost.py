# pcost.py
#
# Exercise 1.27
#Write a program called pcost.py that 
#opens this file,
#reads all lines, and 
#calculates how much it cost to purchase all of the shares in the portfolio.
#TODO Sloppy add in last line. Correct with for loop to look for int and float to total

#Exercise 1.31
#Modify the pcost.py program to catch the exception (missing.csv), print a warning message, and continue processing the rest of the file.
import csv
import sys

def portfolio_cost(filename):

    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
                print(row)
                #break                
                    
            except ValueError:
                print(f'Row {rowno}: Bad data in row: {row}')  #New error
                #print("Value data missing for", row[0], "row.") # Old error
                #break
    return total_cost
            

def main():
    filename = 'Data/portfoliodate.csv'
    cost = portfolio_cost(filename)
    print('Total cost:', cost)
        
        
if __name__ == "__main__":
    main()