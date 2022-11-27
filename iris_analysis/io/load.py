import csv

def load1(path):
    with open(path) as file:
        csvreader = csv.reader(file)
        line_count = 0
        for row in csvreader:
            if line_count == 0:
                print(f'Nazwy kolumn to: {", ".join(row)}')
                line_count += 1
            else:
                print(f'sepal length {row[0]} \tsepal width {row[1]} \tpetal length {row[2]} \tpetal width {row[3]} \tvariety {row[4]}.')
                line_count += 1
        print(f' {line_count} obserwacji.')




def load2(path):
    with open(path) as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
