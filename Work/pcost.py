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
        for row in rows:
            while True:
                try:
                    nshares = int(row[1])
                    price = float(row[2])
                    total_cost += nshares * price
                    print("Data for", row[0], "added.")
                    break
                except ValueError:
                    print("Value data missing for", row[0], "row.")
                    break
    return total_cost
            

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'
    cost = portfolio_cost(filename)
    print('Total cost:', cost)
        
        
if __name__ == "__main__":
    main()