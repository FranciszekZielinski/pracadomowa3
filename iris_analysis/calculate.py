import csv
from collections import defaultdict
import statistics

columns = defaultdict(list)
def stats():
    with open("iris.csv") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            for (i, v) in enumerate(row):
                columns[i].append(v)
    mean0 = statistics.mean(float(s) for s in columns[0])
    median0 = statistics.median(float(s) for s in columns[0])
    std0 = statistics.stdev(float(s) for s in columns[0])
    mean1 = statistics.mean(float(s) for s in columns[1])
    median1 = statistics.median(float(s) for s in columns[1])
    std1 = statistics.stdev(float(s) for s in columns[1])
    mean2 = statistics.mean(float(s) for s in columns[2])
    median2 = statistics.median(float(s) for s in columns[2])
    std2 = statistics.stdev(float(s) for s in columns[2])
    mean3 = statistics.mean(float(s) for s in columns[3])
    median3 = statistics.median(float(s) for s in columns[3])
    std3 = statistics.stdev(float(s) for s in columns[3])
    return mean0, mean1, mean2, mean3, median0, median1, median2, median3, std0, std1, std2, std3


