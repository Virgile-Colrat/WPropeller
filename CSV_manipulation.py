import csv

header=["Angle","Distance"]
def ReturnX(i):
	reader = csv.reader(open('dataX.csv', newline=''), delimiter=',')
	return(reader[i][1])
	
def addDataY(dataLine):
	with open('dataY.csv','a', newline='') as main:
		csv_writer=csv.writer(main, delimiter=",")
		csv_writer.writerow(dataLine)
def addDataX(dataLine):
	with open('dataX.csv','a', newline='') as main:
		csv_writer=csv.writer(main, delimiter=",")
		csv_writer.writerow(dataLine)

def createCsvY():
	with open('dataY.csv','w', newline='') as main:
		csv_writer=csv.writer(main, delimiter=",")
		csv_writer.writerow(header)

def createCsvX():
	headerX=["number","X value"]
	with open('dataX.csv','w', newline='') as main:
		csv_writer=csv.writer(main, delimiter=",")
		csv_writer.writerow(headerX)
