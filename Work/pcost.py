# pcost.py
#
# Exercise 1.27

# TODO: allow user to select what type of files to read from command prompt
import csv
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


def portfolio_cost(file):
    total_cost = 0

    with open(file, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except:
                print(f'Row {rowno}: Missing data: {row}')
            # try:
            #     stock, share, price = row
            #     total_cost += int(share) * float(price)
            # except:
            #     print(f'Missing data: {row}')

    return total_cost


cost = portfolio_cost(filename)

print(f'Total cost: {cost}')
