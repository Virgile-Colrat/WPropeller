import csv

header=["Angle","Distance"]

def addData(dataLine):
	with open('data.csv','a') as main:
		csv_writer=csv.writer(main, delimiter=",")
		csv_writer.writerow(dataLine)

def createCsv():
	with open('data.csv','w') as main:
		csv_writer=csv.writer(main, delimiter=",")
		csv_writer.writerow(header)