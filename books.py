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

#.Run books.csv
def run_books():
    data = read_books_data()

    #Finding top 3 book ratings
    ratings_list = data
    #sorted_ratings_list = ratings_list.sort(key=myFunc, reverse=True)
    ratings_list.sort(key=myFunc, reverse=True)
    print(ratings_list[:3])


    # Get only name, author and avg ratings



    # Search by publisher name, get book title
    publisher_list = data
    book_title_by_pub = []

    for row in publisher_list:

        if row['publisher'] == 'Oxford University Press':
            row_book_pub = []
            row_book_pub = [row['title'],row['publisher']]
            book_title_by_pub.append(row_book_pub)

    print(book_title_by_pub)




run_books()

