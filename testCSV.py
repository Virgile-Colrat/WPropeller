import csv
inputFile = 'dataX.csv'
reader = csv.reader(open(inputFile, newline=''), delimiter=',')

for row in reader:
    print(row)