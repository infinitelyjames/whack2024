import matplotlib.pyplot as plt
import numpy as np
import os

class DataManager:
    graphDict = {"1MSFT.csv":"Microsoft", "1TZOO.csv":"Travel Zoo",  "FTSE 100 Historical Data.csv":"FTSE 100","S&P 500 Historical Data.csv":"S&P 500"}
    dataDict = {}

    @staticmethod
    def loadFromFile():
        fileArr = os.listdir("data")
        for strName in fileArr:
            arr=[] #creating the array
            filename = "data/"+strName
            if strName[0]=="1":
                arr = np.loadtxt(filename, delimiter=",", dtype=str, skiprows= 0, usecols=2)
                arr05 = []
                for i in range(len(arr)-1,0,-1):
                    temp = (arr[i])[:-4]
                    arr05.append(int(temp[1:])/100)
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
    def displayResults(month:int, year:int, company:str):
        arr = DataManager.dataDict[company]
        tempX = []
        tempY = []
        for i in range((12*year)+month):
            tempY.append(arr[i])
            tempX.append(i)
        xpoints = np.array(tempX)
        ypoints = np.array(tempY)
        plt.plot(xpoints, ypoints)
        plt.savefig(f"static/{company}.png")

def main():
    DataManager.loadFromFile()
    DataManager.displayResults(8, 19, 'Microsoft')

if __name__ == "__main__":
    main()