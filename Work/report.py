# report.py
#
# Exercise 2.4

# Exercise 2.16
# Modify the report.py program you wrote in Section 2.3 so that it uses the same technique to pick out column headers.
# Try running the report.py program on the Data/portfoliodate.csv file and see that it produces the same answer as before.



import csv

def portfolio_cost(filename):
    total_cost = 0.0
    #total_cost is an string type integer
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            nshares = int(record['shares'])
            price = float(record['price'])
            total_cost += nshares * price
    return total_cost

def read_portfolio(filename):
    total_cost = []
    #total_cost is a list
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            nshares = int(record['shares'])
            price = float(record['price'])
            total_cost += nshares
            * price  #list doesn't let floats to be iterable
    return portfolio

def main():
    filename = 'Data\portfoliodate.csv'
    total_cost = portfolio_cost(filename)
    print(read_portfolio(filename))
    
if __name__ == '__main__':
    main()