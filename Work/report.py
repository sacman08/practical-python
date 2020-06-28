# report.py
#
# Exercise 2.4



import csv
filename = 'Data\portfolio.csv'
def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost

def read_portfolio(filename):
    total_cost = []
    for row in rows:
        holding = (row[0], int(row[1]), float(row[2]))
        portfolio.append(holding)
    return portfolio

print(read_portfolio(filename))