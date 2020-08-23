import csv
import random
import numpy as np
import matplotlib.pyplot as plt

# Dataset: books.csv

# Analysis Steps:
# 1. Read data from CSV file
# 2. Display top 3 books - title, author, average ratings
# 3. Search a book title by  publisher name.
# 4. Display book title, author, pages as short reads (maximum pages 100)
# 5. Display random book of the day
# 6. Write all the findings in a text file
# 7. Display a Graph

#1. Read books data from CSV:
def read_books_data():
    data = []

    with open('books.csv', 'r') as books_csv:
        spreadsheet = csv.DictReader(books_csv)
        for row in spreadsheet:
            data.append(row)

    return data

# Function to sort a list as per average_ratings
def myFunc(row):
  return row['average_rating']


#.Run books.csv
def run_books():
    data = read_books_data()

    #Finding top 3 book ratings
    ratings_list = data
    ratings_list.sort(key=myFunc, reverse=True)



    # 1.Get only name, author and avg ratings
    top_3 = ratings_list[:3]
    book = []


    for row in top_3:
        top_3_books = []
        top_3_books= [row['title'],row['authors'], row['average_rating']]
        book.append(top_3_books)
    print('Top 3 books : {}'.format(book))

    # 2.Search by publisher name, get book title - 1.(Oxford University Press)
    publisher_list = data
    book_title_by_pub_1 = []

    for row in publisher_list:

        if row['publisher'] == 'Oxford University Press':
            row_book_pub = []
            row_book_pub = [row['title'],row['publisher']]
            book_title_by_pub_1.append(row_book_pub)

    print('Books by Oxford University Press: {}'.format(book_title_by_pub_1))

    # Search by publisher name, get book title - 2.(Penguin Books)
    publisher_list = data
    book_title_by_pub_2 = []

    for row in publisher_list:

        if row['publisher'] == 'Penguin Books':
            row_book_pub = []
            row_book_pub = [row['title'], row['publisher']]
            book_title_by_pub_2.append(row_book_pub)

    print('Books by Penguin Books: {}'.format(book_title_by_pub_2))

    # Search by publisher name, get book title - 3.(Harper)
    publisher_list = data
    book_title_by_pub_3 = []

    for row in publisher_list:

        if row['publisher'] == 'Harper Perennial':
            row_book_pub = []
            row_book_pub = [row['title'], row['publisher']]
            book_title_by_pub_3.append(row_book_pub)

    print('Books by Harper: {}'.format(book_title_by_pub_3))

    # short reads - Finding books with 100 pages:
    page_list = data
    book_short_read = []



    for row in page_list:

         if int(row['  num_pages']) <= 100:
             short = []
             short = [row['title'],row['authors'], row['  num_pages']]

             book_short_read.append(short)

    print('SHORT READS (Upto 100 pages): {}'.format(book_short_read))

    # Random: book of the day
    chosen_book = random.choice(data)
    print('Random book of the day: {}'.format(chosen_book))


    # Writing top 3 ratings to a file
    with open('analysis_books.txt', 'w') as f:
        print('\n \n \n----BOOKS DATASET ANALYSIS---- ', file=f)
        print('\n \n \nTop 3 Ratings:', '\n','\n','\n', book, file=f)
        print('\n \n \nBook by publisher - 1:', '\n', '\n', '\n', book_title_by_pub_1, file=f)
        print('\n \n \nBook by publisher - 2:', '\n', '\n', '\n', book_title_by_pub_2, file=f)
        print('\n \n \nBook by publisher - 3:', '\n', '\n', '\n', book_title_by_pub_3, file=f)
        print('\n \n \nShort Reads:', '\n', '\n', '\n', book_short_read, file=f)
        print('\n \n \nRandom book of the day :', '\n', '\n', '\n', chosen_book, file=f)

    # GRAPH: Book Name and Ratings:
    # Make a dataset:
    avg_ratings = (5, 4.6, 4.5)
    books = ('Middlesex Borough', 'Stories and Early Novels','Love You Until')
    y_pos = np.arange(len(books))

    # Create bars
    plt.bar(y_pos, avg_ratings)

    # Create names on the x-axis
    plt.xticks(y_pos, books)

    # Show graphic
    plt.savefig("mygraph.png")
    plt.show()


run_books()

