import csv
import random
import numpy as np
import matplotlib.pyplot as plt


# Business Question: Is there a correlation between sales
# and expenditure to the profit or loss of sales in each month

#1. Read sales data from spreadsheet
def read_sales_data():
    sales_data = []

    with open('sales.csv', 'r') as sales_csv:
        sales_spreadsheet = csv.DictReader(sales_csv)
        for row in sales_spreadsheet:
            sales_data.append(row)

    return sales_data


#2. Function to calculate percentage change between sales and expenditure in a month
def percentage(sales,expenditures):
    difference = (sales - expenditures)
    change = (difference / sales)
    percentage = change * 100

    return (round(percentage, 2))


#Function to calculate difference between sales and expenditure
def profit_loss(sales, expenditures):
    if sales > expenditures:
        amount = sales - expenditures
        print('Profit: {}'.format(amount))
    elif sales < expenditures:
        amount = sales - expenditures
        print('Loss: {}'.format(amount))
    else:
        print('Same')

    return amount


# 3.Sales analysis
def run_sales():
    data = read_sales_data()

    #Collect all sales in a list
    sales = []

    for row in data:
        sale = int(row['sales'])
        sales.append(sale)


    #Writing the output to the file
    with open('analysis_sales.txt', 'w') as f:
        print("*********** SALES ANALYSIS REPORT - 2018 ***********", file=f)
        print('\nAll Sales:', sales, file=f)

    # Collect all expenditures in a list
    expenditures = []

    for row in data:
        spending = int(row['expenditure'])
        expenditures.append(spending)


    #Writing the output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\nAll Expenditures:', expenditures, file=f)

    # Collect all months in a list
    month = []

    for row in data:
        sale = (row['month'])
        month.append(sale)


    # Output total sales for all months
    total = sum(sales)


    #Writing the output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\nTotal sales:', total, file=f)

    # Output total sales for all months
    total_exp = sum(expenditures)


    # Writing the output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\nTotal Expenditure:', total_exp, file=f)

    # Output average for all months
    average = total / len(sales)


    #Writing the output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\nAverage sales:', (round(average)), file=f)


    # ****MIN-MAX SALES****

    # Minimum Sales: Writing the output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \nMinimum sales:', (min(sales)), file=f)


    # Minimum Sales: Finding the index of Min sales

    min_value = 1521
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', sales.index(min_value), file=f)

    # Minimum Sales: Using the index to find the min sales month
    min_sales_month = month[1]
    with open('analysis_sales.txt', 'a') as f:
        print('\nMonth with minimum sales:', min_sales_month, file=f)



    # Maximun Sales: Writing the output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \nMaximum sales:', (max(sales)), file=f)

    # Maximun Sales: Finding the index of Max sales
    max_value = 7479
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', sales.index(max_value), file=f)

    # Maximun Sales: Using the index to find the max sales month
    max_sales_month = month[6]
    with open('analysis_sales.txt', 'a') as f:
        print('\nMonth with maximum sales:', max_sales_month, file=f)


    # ****MIN-MAX EXPENDITURE****

    # Minimum Expenditure: Writing the output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \nMinimum expenditure:', (min(expenditures)), file=f)

    # Minimum Expenditure: Finding the index of Min Expenditure
    min_value = 1098
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', expenditures.index(min_value), file=f)

    # Minimum Expenditure: Using the index to find the min Expenditure month
    min_exp_month = month[3]
    with open('analysis_sales.txt', 'a') as f:
        print('\nMonth with minimum expenditures:', min_exp_month, file=f)



    # Maximum Expenditure: Writing the output to the file
    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \nMaximum expenditure:', (max(expenditures)), file=f)


    # Maximum Expenditure: Finding the index of Max Expenditure
    max_value = 3965
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', expenditures.index(max_value), file=f)

    # Maximum Expenditure: Using the index to find the max Expenditure month
    man_exp_month = month[2]
    with open('analysis_sales.txt', 'a') as f:
        print('\nMonth with maximum expenditures:', man_exp_month, file=f)



    # Summerising Rest of the month Sales
    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \n----PERCENT CHANGE OF SALES AS PER MONTHS---- ', file=f)
        print('\n \n \n----JANUARY---- ', file=f)
        print('\nPercent Change:', (percentage(sales[0], expenditures[0])), file=f)
        print('\n \n \n----FEBRUARY---- ', file=f)
        print('\nPercent Change:', (percentage(sales[1], expenditures[1])), file=f)
        print('\n \n \n----MARCH---- ', file=f)
        print('\nPercent Change:', (percentage(sales[2], expenditures[2])), file=f)
        print('\n \n \n----APRIL---- ', file=f)
        print('\nPercent Change:', (percentage(sales[4], expenditures[4])), file=f)
        print('\n \n \n----MAY---- ', file=f)
        print('\nPercent Change:', (percentage(sales[4], expenditures[4])), file=f)
        print('\n \n \n----JUNE---- ', file=f)
        print('\nPercent Change:', (percentage(sales[5], expenditures[5])), file=f)
        print('\n \n \n----JULY---- ', file=f)
        print('\nPercent Change:', (percentage(sales[6], expenditures[6])), file=f)
        print('\n \n \n----AUGUST---- ', file=f)
        print('\nPercent Change:', (percentage(sales[7], expenditures[7])), file=f)
        print('\n \n \n----SEPTEMBER---- ', file=f)
        print('\nPercent Change:', (percentage(sales[8], expenditures[8])), file=f)
        print('\n \n \n----OCTOBER---- ', file=f)
        print('\nPercent Change:', (percentage(sales[9], expenditures[9])), file=f)
        print('\n \n \n----NOVEMBER---- ', file=f)
        print('\nPercent Change:', (percentage(sales[10], expenditures[10])), file=f)
        print('\n \n \n----DECEMBER---- ', file=f)
        print('\nPercent Change:', (percentage(sales[11], expenditures[11])), file=f)






    # Summerising 2018
    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \n----SUMMERY OF 2018---- ', file=f)
        print('\nTotal Sales:', total, file=f)
        print('\nTotal Expenditure:', total_exp, file=f)
        print('\nProfit/Loss:', profit_loss(total, total_exp), file=f)
        print('\nPercent Change:', percentage(total, total_exp), file=f)

# Making a new csv file.
    field_names = ['month',  'percent_change', 'Observation']
    data = [
        {'month': 'Jan', 'percent_change':  38.84, 'Observation': ''},
        {'month': 'Feb',  'percent_change':  -121.76, 'Observation': 'Min_Sales'},
        {'month': 'March', 'percent_change':  -115.26,'Observation': 'Max_Exp'},
        {'month': 'April', 'percent_change':  46.47,'Observation': 'Min_Exp'},
        {'month': 'May', 'percent_change': -76.27, 'Observation': ''},
        {'month': 'June', 'percent_change':-5.61, 'Observation': 'Max_Sale'},
        {'month': 'July', 'percent_change':  72.14, 'Observation': ''},
        {'month': 'August', 'percent_change': 62.81, 'Observation': ''},
        {'month': 'September', 'percent_change': 54.38, 'Observation': ''},
        {'month': 'October', 'percent_change': 79.61, 'Observation': ''},
        {'month': 'November', 'percent_change': 80.19, 'Observation': ''},
        {'month': 'December', 'percent_change': -94.92, 'Observation': ''},

    ]

    with open('observation.csv', 'w+') as csv_file:
         spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
         spreadsheet.writeheader()
         spreadsheet.writerows(data)

    #Plotting the percentage difference on graph
    # Make a fake dataset:
    observation = (38.84,-121.76,-115.26,46.47,-76.27,
                    -5.61,72.14,62.81,54.38,79.61,80.19,-94.92)

    month = ('JAN', 'FEB', 'MARCH', 'APRIL','MAY', 'JUNE',
             'JULY', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')
    y_pos = np.arange(len(month))



    # Create bars
    plt.bar(y_pos, observation)

    # Create names on the x-axis
    plt.xticks(y_pos, month)

    # Show graphic
    plt.savefig("mygraph.png")
    plt.show()


run_sales()


# Dataset 2: books.csv
# Business Question: Is there a correlation between authour
# and ratings?

#1. Read books data from spreadsheet
def read_books_data():
    data = []

    with open('books.csv', 'r') as books_csv:
        spreadsheet = csv.DictReader(books_csv)
        for row in spreadsheet:
            data.append(row)

    return data

def run_books():
    data = read_books_data()

    #Collect all books in a list
    all_books = []
    for row in data:
        all_books.append(data)

    #Collect all book titles in a list
    title = []
    for row in data:
        book_data = (row['title'])
        title.append(book_data)

    # Collect all book authors in a list
    author = []
    for row in data:
        author_data = (row['authors'])
        author.append(author_data)

    # Collect all book ratings in a list
    ratings = []
    for row in data:
        rating_data = int(row['ratings_count'])
        ratings.append((rating_data))

    #Finding top 5 book ratings
    sorted_ratings_list = sorted(ratings, reverse=True) # note sort and sorted diff
    top_3_ratings = (sorted_ratings_list[:3])

    #Writing top 3 ratings to a file
    with open('analysis_sales.txt', 'a') as f:
        print('\n \n \n----BOOKS DATASET---- ', file=f)
        print('\nTop 3 Ratings:', top_3_ratings, file=f)

    # Finding the index of top 1 rating book
    top_1 = 2128944
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', ratings.index(top_1), file=f)

    # Using the index to find the name of book
    top_1_bookname = title[90]
    with open('analysis_sales.txt', 'a') as f:
         print('\nNo.1 Book Name:', top_1_bookname, file=f)

    # Using the index to find the name of the author
    top_1_authorname = author[90]
    with open('analysis_sales.txt', 'a') as f:
         print('\nNo.1 Book - Author:', top_1_authorname, file=f)

    # Finding the index of top 2 rating book
    top_2 = 613758
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', ratings.index(top_2), file=f)

    # Using the index to find the name of book
    top_2_bookname = title[7]
    with open('analysis_sales.txt', 'a') as f:
        print('\nNo.2 Book Name:', top_2_bookname, file=f)

    # Using the index to find the name of the author
    top_2_authorname = author[7]
    with open('analysis_sales.txt', 'a') as f:
        print('\nNo.2 Book - Author:', top_2_authorname, file=f)

    # Finding the index of top 3 rating book
    top_3 = 308840
    with open('analysis_sales.txt', 'a') as f:
        print('\nIndex:', ratings.index(top_3), file=f)

    # Using the index to find the name of book
    top_3_bookname = title[81]
    with open('analysis_sales.txt', 'a') as f:
        print('\nNo.3 Book Name:', top_3_bookname, file=f)

    # Using the index to find the name of the author
    top_3_authorname = author[81]
    with open('analysis_sales.txt', 'a') as f:
        print('\nNo.3 Book - Author:', top_3_authorname, file=f)

    # Random: book of the day
    chosen_book = random.choice(title)
    with open('analysis_sales.txt', 'a') as f:
        print('\nBook of the day:', chosen_book, file=f)



run_books()

