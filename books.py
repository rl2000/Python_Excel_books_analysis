import csv

def read_sales_data():
    sales_data = []

    with open('sales.csv', 'r') as sales_csv:
        sales_spreadsheet = csv.DictReader(sales_csv)
        for row in sales_spreadsheet:
            sales_data.append(row)

    return sales_data

def percentage_decrease(month_1, month_2):
    decrease = (month_1 - month_2)
    difference = (decrease / month_1)
    percentage_decrease = difference * 100

    return percentage_decrease

def run_sales():
    data = read_sales_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    print('All of the sales from Jan to Dec 2018: {}'.format(sales))

    total = sum(sales)
    print('Total sales across all months: {}'.format(total))

    average = total / len(sales)
    print('Average sales from Jan to Dec: {}'.format(round(average)))

    print('Minimum sales in a year : {}'. format(min(sales)))

    print('Maximum sales in a year : {}'. format(max(sales)))

    percentage_decrease(sales[0], sales[6])
    print('Percentage decrease difference between Jan and Jun Sales: '
          '{}'.format((percentage_decrease(sales[0], sales[6]))))

    percentage_decrease(sales[0], sales[11])
    print('Percentage decrease difference between Jan and Dec Sales: '
          '{}'.format((percentage_decrease(sales[0], sales[11]))))


run_sales()

