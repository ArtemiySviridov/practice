import csv


def write_to_csv_file(name_of_file):
    print("---------------------------------------------------------")
    data = []
    quantity_of_new_rows = int(input("Enter quantity of new rows: "))

    for rows in range(0, quantity_of_new_rows):
        book_name = input("Enter book name: ")
        book_author = input("Enter book author: ")
        book_publishing_year = int(input("Enter publishing year: "))
        excel_row = [book_name, book_author, book_publishing_year]
        data.append(excel_row)

    with open(name_of_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(data)
    print("---------------------------------------------------------")


def read_from_csv_file(name_of_file):
    print("---------------------------------------------------------")
    enter_author_to_find = input("Enter author to find: ")
    found_books = []
    with open(name_of_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if enter_author_to_find == row['Author']:
                found_books.append(row)

    if len(found_books) > 0:
        print("All books of entered author: ")
        for book in found_books:
            book_string = ', '.join(book.values())
            print(book_string)
    print("---------------------------------------------------------")


def find_book_in_year_range(name_of_file):
    low_limit = int(input("Enter lower limit of publishing year: "))
    high_limit = int(input("Enter higher limit of publishing year: "))
    found_books_in_range_of_years = []
    with open(name_of_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            for year in range(low_limit, high_limit + 1):
                year = str(year)
                if year == row['Publishing year']:
                    found_books_in_range_of_years.append(row)

    if not found_books_in_range_of_years:
        print("There are no books in this range!")
    else:
        print("All books of entered range: ")
        for book in found_books_in_range_of_years:
            book_string = ', '.join(book.values())
            print(book_string)
    print("---------------------------------------------------------")


def main():
    filename = 'books.csv'

    print("---------------------------------------------------------")
    print("1. Add new book.")
    print("2. Find all books of entered author.")
    print("3. Find all books in range of entered publishing years.")
    print("---------------------------------------------------------")

    while True:
        menu = int(input("Enter number of option: "))
        match menu:
            case 1:
                write_to_csv_file(filename)
                break
            case 2:
                read_from_csv_file(filename)
                break
            case 3:
                find_book_in_year_range(filename)
                break
    print("---------------------------------------------------------")


main()
