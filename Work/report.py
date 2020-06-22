# report.py
#
# Exercise 2.4
import csv
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


def read_portfolio(file):
    # total_cost = 0
    portfolio = []

    with open(file, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)

        for row in rows:
            try:
                holding = {'name': row[0], 'shares': int(row[1]), 'price': float(row[2])}
                portfolio.append(holding)
                # portfolio.append((row[0], int(row[1]), float(row[2])))

            except:
                print(f'Missing data: {row}')

    return portfolio

def read_prices(file):
    prices = {}

    with open(file, 'rt') as f:
        rows = csv.reader(f)
        # headers = next(rows)
        # print(headers)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
                # portfolio.append((row[0], int(row[1]), float(row[2])))

            except:
                print(f'Missing data: {row}')

    return prices

def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        current_price = prices[name]
        change = prices[name] - stock['price']

        summary = (name, shares, current_price, change)
        report.append(summary)

    return report


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f'---------- ---------- ---------- -----------')
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
    # print(f'{name} {shares} {price} {change}')




