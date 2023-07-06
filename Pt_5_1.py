import csv
data = [
    ['Name', 'Author', 'Publishing year'],
    ['The Notebook', 'Nicholas Sparks', '1996'],
    ['The Choice', 'Nicholas Sparks', '2007'],
    ['Brief Answers to the Big Questions', 'Stephen Hawking', '2018'],
    ['The Black Flag', 'Oliver Bowden', '2013'],
    ['Renaissance', 'Oliver Bowden', '2009']
]

filename = 'books.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data)
