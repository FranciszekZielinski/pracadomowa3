from iris_analysis.calculate import stats
import iris_analysis.io.load
import csv


def save(header, data):
    with open('results.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)



