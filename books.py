import csv
import random

############################################################################################
def read_sales_data():
    sales_data = []

    with open('sales.csv', 'r') as sales_csv:
        sales_spreadsheet = csv.DictReader(sales_csv)
        for row in sales_spreadsheet:
            sales_data.append(row)

    return sales_data
##########################################################################################
#Function to calculate percentage difference
def percentage_decrease(new_no, original_no):
    decrease = (original_no - new_no)
    difference = (decrease / original_no)
    percentage_decrease = difference * 100

    return percentage_decrease
##############################################################################################

#Function to calculate percentage difference
def percentage_increase(new_no, original_no):
    increase = (new_no - original_no)
    increase_difference = (increase / new_no)
    percentage_increase = increase_difference * 100

    return percentage_increase

########################################################################################

    #Function to calculate profit
def profit(sales, expenditures):
    if sales > expenditures:
        amount = sales - expenditures
        print('Profit: {}'.format(amount))
    elif sales < expenditures:
        amount = sales - expenditures
        print('Loss: {}'.format(amount))
    else:
        print('Same')

    return amount






####################################################################################################
def run_sales():
    data = read_sales_data()

    sales = []

    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    print('All of the sales from Jan to Dec 2018: {}'.format(sales))

    #copying the print output to the file
    with open('analysis_sales.txt', 'w') as f:
        print("******SALES ANALYSIS - 2018******", file=f)
        print('\nAll of the sales from Jan to Dec 2018:', sales, file=f)

#############################################################################################
    expenditures = []

    for row in data:
        spending = int(row['expenditure'])
        expenditures.append(spending)
    print('All sales expenditures from Jan to Dec 2018: {}'.format(expenditures))

    # copying the print output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\nAll sales expenditures from Jan to Dec 2018:', expenditures, file=f)
############################################################################################

    month = []

    for row in data:
        sale = (row['month'])
        month.append(sale)
    #print('All of the sales from Jan to Dec 2018: {}'.format(month))

    total = sum(sales)
    print('Total sales across all months: {}'.format(total))

    # copying the print output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\nTotal sales across all months:', total, file=f)
#######################################################################################################
    average = total / len(sales)
    print('Average sales from Jan to Dec: {}'.format(round(average)))

    # copying the print output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\nAverage sales from Jan to Dec:', (round(average)), file=f)
######################################################################################
    # copying the print output to the file
    with open('analysis_sales.txt', 'a') as f:

        print('\n \n \nMinimum sales in a year:', (min(sales)), file=f)


    print('Minimum sales in a year : {}'. format(min(sales)))
    min_value = 1521
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', sales.index(min_value), file=f)

    min_sales_month = month[1]
    with open('analysis_sales.txt', 'a') as f:
        print('\nMonth with minimum sales:', min_sales_month, file=f)

    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \nANALYSING FEB SALES ', file=f)

        print('\nSales:', sales[2], file=f)
        print('\nExpenditure:', expenditures[2], file=f)
        print('\nProfit:', (profit(sales[2], expenditures[2])), file=f)



    ##############################################################################################
        # copying the print output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \nMaximum sales in a year:', (max(sales)), file=f)


    max_value = 7479
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', sales.index(max_value), file=f)

    max_sales_month = month[6]
    with open('analysis_sales.txt', 'a') as f:
        print('\nMonth with maximum sales:', max_sales_month, file=f)



    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \n ANALYSING JULY SALES ', file=f)
        print('\nSales:', sales[7], file=f)
        print('\nExpenditure:', expenditures[7], file=f)
        print('\nProfit:', (profit(sales[7], expenditures[7])), file=f)



    ##################################################################################################

    # copying the print output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \n % INCREASE BETWEEN FEB AND JULY SALES IN 2018', file=f)

        print('\nResult:',(round(percentage_increase(sales[7], sales[1]),2)), file=f)


#####################################################################################################

#business q:  is there a correlation between sales and expenditure and the profit going up or down.

#######################################################################################




    # percentage_decrease(sales[0], sales[1])
    # print("Jan-Feb sales decreased by %: {}".format(round(percentage_decrease(sales[0], sales[6]), 2)))
    #
    #
    # percentage_decrease(sales[1], sales[2])
    # print("Feb-March sales decreased by %: {}".format(round(percentage_decrease(sales[1], sales[2]), 2)))
    #
    # percentage_decrease(sales[2], sales[3])
    # print("March-April sales decreased by %: {}".format(round(percentage_decrease(sales[2], sales[3]), 2)))
    #
    # percentage_decrease(sales[3], sales[4])
    # print("April-May sales decreased by %: {}".format(round(percentage_decrease(sales[3], sales[4]), 2)))
    #
    # percentage_decrease(sales[4], sales[5])
    # print("May-June sales decreased by %: {}".format(round(percentage_decrease(sales[4], sales[5]), 2)))
    #
    # percentage_decrease(sales[5], sales[6])
    # print("June-July sales decreased by %: {}".format(round(percentage_decrease(sales[5], sales[6]), 2)))
    #
    # percentage_decrease(sales[6], sales[7])
    # print("July-Aug sales decreased by %: {}".format(round(percentage_decrease(sales[6], sales[7]), 2)))
    #
    # percentage_decrease(sales[7], sales[8])
    # print("Aug-Sep sales decreased by %: {}".format(round(percentage_decrease(sales[6], sales[7]), 2)))
    #
    # percentage_decrease(sales[8], sales[9])
    # print("Sep-Oct sales decreased by %: {}".format(round(percentage_decrease(sales[8], sales[9]), 2)))
    #
    # percentage_decrease(sales[9], sales[10])
    # print("Oct-Nov sales decreased by %: {}".format(round(percentage_decrease(sales[9], sales[10]), 2)))
    #
    # percentage_decrease(sales[10], sales[11])
    # print("Nov-Dec sales decreased by %: {}".format(round(percentage_decrease(sales[10], sales[11]), 2)))
    #
    # #print('Maximum expenditure in a year : {}'.format(max(expenditures)))


run_sales()
print("*"* 50)
#############################################################################################
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

    # copying the print output to the file




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

    # print('Book with maximum ratings: {}'. format(max(ratings)))
    #
    # top_3_books = sorted(zip(ratings, title), reverse=True)[:3]
    # print("Top 3 books with highest ratings:{}".format(top_3_books))

    # with open('analysis_sales.txt', 'a') as f:
    #     print("\n \n \n****** BOOKS ANALYSIS ******", file=f)
    #     print('\nTOP 3 BOOKS:', top_3_books, file=f)

    #top 5 book ratings
    sorted_ratings_list = sorted(ratings, reverse=True) # note sort and sorted diff

    top_3 = (sorted_ratings_list[:3])
    with open('analysis_sales.txt', 'a') as f:
        print("\n \n \n****** BOOKS ANALYSIS ******", file=f)
        print('\nTop 3 ratings of books:',top_3, file=f)


    print(ratings)
    top_1_index = 2128944
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', ratings.index(top_1_index), file=f)

    top_1_book = title[98]
    with open('analysis_sales.txt', 'a') as f:
         print('\nNo.1 book:', top_1_book, file=f)

    author_book_1 = author[98]
    with open('analysis_sales.txt', 'a') as f:
        print('\nAuthor:', author_book_1, file=f)

    top_2_index = 613758
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', ratings.index(top_2_index), file=f)

    # top_1_book = title[98]
    # with open('analysis_sales.txt', 'a') as f:
    #     print('\nNo.1 book:', top_1_book, file=f)
    #
    # author_book_1 = author[98]
    # with open('analysis_sales.txt', 'a') as f:
    #     print('\nAuthor:', author_book_1, file=f)

    chosen_book = random.choice(title)
    print('Random book of the day: {}'.format(chosen_book))



run_books()

