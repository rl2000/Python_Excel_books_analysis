import csv
import random
import numpy as np
import matplotlib.pyplot as plt

# Dataset: books.csv


#1. Read books data from spreadsheet
def read_books_data():
    data = []

    with open('books.csv', 'r') as books_csv:
        spreadsheet = csv.DictReader(books_csv)
        for row in spreadsheet:
            data.append(row)

    return data

#Function to sort a list as per average_ratings
def myFunc(e):
  return e['average_rating']

def myFunc_1(x):
  return x['  num_pages']

#.Run books.csv
def run_books():
    data = read_books_data()

    #Finding top 3 book ratings
    ratings_list = data
    #sorted_ratings_list = ratings_list.sort(key=myFunc, reverse=True)
    ratings_list.sort(key=myFunc, reverse=True)
    print(ratings_list[:3])


    # Get only name, author and avg ratings
    top_3 = ratings_list[:3]
    book = []


    for row in top_3:
        top_3_books = []
        top_3_books= [row['title'],row['authors'], row['average_rating']]
        book.append(top_3_books)
    print(book)

    # Search by publisher name, get book title
    publisher_list = data
    book_title_by_pub = []

    for row in publisher_list:

        if row['publisher'] == 'Oxford University Press':
            row_book_pub = []
            row_book_pub = [row['title'],row['publisher']]
            book_title_by_pub.append(row_book_pub)

    print(book_title_by_pub)

    #short reads
    # Finding books with 100 pages
    page_list = data
    book_short_read = []
    print(page_list)


    for row in page_list:
    #
         if int(row['  num_pages']) <= 100:
             short = []
             short = [row['title'], row['  num_pages']]
             #page_list.sort(key=myFunc_1, reverse=True)
             book_short_read.append(short)

    print('SHORT: {}'.format(book_short_read[:10]))



run_books()

