import matplotlib.pyplot as plt
import numpy as np
import os

class DataManager:
    graphDict = {"Microsoft":"IMSFT.csv", "Travel Zoo" : "ITZOO.csv", "FTSE 100" : "FTSE 100 Historical Data", "S&P 500": "S&P 500 Historical Data"}
    dataDict = {}

    @staticmethod
    def loadFromFile():
        fileArr = os.listdir("data")
        # using loadtxt()
        for str in fileArr:
            arr=[] #creating the array
            filename = "data/"+str
            #filename = "1MSFT.csv"
            if str[0]=="1":
                arr = np.loadtxt(filename, delimiter=",", dtype=str, skiprows= 1, usecols=2)
                arr05 = []
                print(arr)
                for i in range(len(arr)-1,0,-1):
                    temp = (arr[i])[:-4]
                    arr05.append(int(temp[1:]))
                arr = arr05.copy()
            else:
                arr = np.loadtxt(filename,delimiter=",", dtype=str, skiprows= 1, usecols=(3,2))
                arr05 = []
                for i in range(len(arr)-1,0,-1):
                    temp = (arr[i][0]+arr[i][1])[:-4]
                    arr05.append(int(temp[1:]))
                arr = arr05.copy()
        DataManager.dataDict[str] = arr

    #displaying our result.
    @staticmethod
    def displayResults(month:int, year:int, company:str):
        tempStr = DataManager.graphDict[company]
        arr = DataManager.dataDict[tempStr]
        temp = []
        for i in range((12*year)+month):
            temp.append(arr[i])
        xpoints = np.array(temp)
        ypoints = np.array(arr)
        plt.plot(xpoints, ypoints)
        plt.savefig(f"static/{tempStr}.png")