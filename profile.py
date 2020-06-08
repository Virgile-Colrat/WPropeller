import CSV_manipulation
import math
res=800
dataLine=["",""] #Stores the angle and distance
dataX=["",""]
totalLength=75 #=70+5
lengthStrait=70
lengthRound=75
def ComputeProfileY(o):
    x=CSV_manipulation.ReturnX(10)
    print(x)
def ComputeWidths():
    CSV_manipulation.createCsvX()
    x=0
    i=1
    while x < totalLength:
        dataX[0]=i
        if x < lengthStrait:
            dataX[1]=str(round(-0.03*x+7,2))
            CSV_manipulation.addDataX(dataX)
        else:
            dataX[1]=str(round(math.sqrt((5**2)-((x-70)**2)),2))
            CSV_manipulation.addDataX(dataX)
        x=x+0.5
        i=i+1

        
def ComputeEntireProfile(resolutionX):
    ComputeWidths()
    CSV_manipulation.createCsvY()
    for i in range(resolutionX):
        ComputeProfileY(i)