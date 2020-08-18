import csv
import random
# import pandas as pd
# import numpy as np
# df = pd.read_csv('books.csv')
# print(df.dtypes)

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

    percentage_decrease(sales[0], sales[1])
    print("Jan-Feb sales decreased by %: {}".format(round(percentage_decrease(sales[0], sales[6]), 2)))

    percentage_decrease(sales[1], sales[2])
    print("Feb-March sales decreased by %: {}".format(round(percentage_decrease(sales[1], sales[2]), 2)))

    percentage_decrease(sales[2], sales[3])
    print("March-April sales decreased by %: {}".format(round(percentage_decrease(sales[2], sales[3]), 2)))

    percentage_decrease(sales[3], sales[4])
    print("April-May sales decreased by %: {}".format(round(percentage_decrease(sales[2], sales[3]), 2)))


run_sales()
print("*"* 50)

# Dataset 2: books.csv

def read_books_data():
    data = []

    with open('books.csv', 'r') as books_csv:
        spreadsheet = csv.DictReader(books_csv)
        for row in spreadsheet:
            data.append(row)

    return data

def run_books():
    data = read_books_data()

    books = []
    for row in data:
        books.append(data)
    # print('All books_: {}'.format(books))





    title = []
    for row in data:
        book_data = (row['title'])
        title.append(book_data)
    print('All book titles: {}'.format(title))

    author = []
    for row in data:
        author_data = (row['authors'])
        author.append(author_data)
    print('All book authors: {}'.format( author))

    ratings = []
    for row in data:
        rating_data = int(row['ratings_count'])
        ratings.append((rating_data))
        ratings.sort()
    print('All ratings:{}'.format(ratings))

    print('Book with maximum ratings: {}'. format(max(ratings)))

    top_3_books = sorted(zip(ratings, title), reverse=True)[:3]
    print("Top 3 books with highest ratings:{}".format(top_3_books))


    chosen_book = random.choice(title)
    print('Random book of the day: {}'.format(chosen_book))



run_books()

