import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os
from Source.background import create_thread

matplotlib.use('Agg') # DO NOT REMOVE, THIS IS NEEDED FOR THREAD-SAFETY

class DataManager:
    graphDict = {"1MSFT.csv":"Microsoft", "1TZOO.csv":"Travel Zoo",  "FTSE 100 Historical Data.csv":"FTSE 100","S&P 500 Historical Data.csv":"S&P 500"}
    dataDict = {}

    @staticmethod
    def loadFromFile():
        fileArr = os.listdir("data")
        for strName in fileArr:
            arr=[] #creating the array
            filename = "data/"+strName
            #Need this if -else statement because the data files that start with 1 are arranged differently
            #to the others
            if strName[0]=="1":
                arr = np.loadtxt(filename, delimiter=",", dtype=str, skiprows= 0, usecols=2)
                arr05 = []
                for i in range(len(arr)-1,0,-1):
                    temp = (arr[i])[:-4]
                    arr05.append(int(temp[1:]))
                arr = arr05.copy()
            else:
                arr = np.loadtxt(filename,delimiter=",", dtype=str, skiprows= 0, usecols=(3,2))
                arr05 = []
                for i in range(len(arr)-1,0,-1):
                    temp = (arr[i][0]+arr[i][1])[:-4]
                    arr05.append(int(temp[1:])/100)
                arr = arr05.copy()
            DataManager.dataDict[DataManager.graphDict[strName]] = arr

    #displaying our result.
    @staticmethod
    def displayResults(month:int, company:str):
        arr = DataManager.dataDict[company]
        #print(arr)
        tempX = []
        tempY = []
        for i in range(month):
            tempY.append(arr[i])
            tempX.append(i)#This is the months for the x-axis
        xpoints = np.array(tempX)
        ypoints = np.array(tempY)
        plt.plot(xpoints, ypoints)
        plt.savefig(f"static/{company}.png")
        plt.close()
    
    @staticmethod
    def getCompanyNames():
        return DataManager.graphDict.values()
    
    @staticmethod 
    def getStockPrice(month:int, company:str):
        arr = DataManager.dataDict[company]
        return arr[month]
    
    @staticmethod
    def displayAllResults(month:int):
        print("Displaying all results for month", month)
        for company in DataManager.graphDict.values():
            DataManager.displayResults(month, company)

def main():
    DataManager.loadFromFile()
    DataManager.displayResults(29, 'Microsoft')
    print(DataManager.getStockPrice(19, "Microsoft"))

if __name__ == "__main__":
    main()