import pickle

class Account:
    """
    INTEREST IS DEPRECATED, DO NOT USE
    IT IS VARIABLE, SO IT WILL NOT BE SAVED
    """
    def __init__(self, name:str, amount:float):
        self.name = name
        self.amount = amount
        self.interest = [4.75,4.65,5.52,4.62,0.63,0.5,0.5,0.5,0.5,0.5,0.5,0.4,0.28,0.59,0.75,0.22,0.1,1.56,4.73,5.18]
 # deprecated
    def updateInterest(self,monthcount):
        tempintrest = self.interest[monthcount // 12]
        self.amount *= (1+tempintrest/(12*100))
        self.amount = round(self.amount,2)
    def addAmount(self, change:float):
        self.amount += change
    def removeAmount(self, change:float):
        self.amount -= change
    @staticmethod
    def loadFromFile(filename:str):
        with open(filename, "rb") as file:
            return pickle.load(file)
    def saveToFile(self, filename:str):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

class StockAccount:
    value = 0

    def __init__(self, name:str, shares:int, sharePrice:float):
        self.name = name
        self.shares = shares
        self.sharePrice = sharePrice
        self.value = shares*sharePrice
        self.buyPrice = 0
        #self.percent = round(((self.value - self.buyPrice)/(self.buyPrice+0.0001))*100, 2)
    def updateShares(self, change:int):
        print(f"INFO: Updating {self.name} shares by {change}, was {self.shares}")
        print(f"DEBUG: Buy price was {self.buyPrice}, share price was {self.sharePrice}, shares were {self.shares}")
        if(change >0):
            self.buyPrice += change * self.sharePrice
        elif(change < 0):
            self.buyPrice += (self.buyPrice/self.shares)*change
        self.shares += change
        self.calculateValue()
    def updateSharePrice(self, change:int):
        self.sharePrice += change
        self.calculateValue()
    def setSharePrice(self, price:float):
        self.sharePrice = price
        self.calculateValue()
    def calculateValue(self):
        self.value = self.shares* self.sharePrice
    def calculatePercentageGain(self):
        self.percent = round(((self.value - self.buyPrice)/(self.buyPrice+0.0001))*100, 2)
        return self.percent
    def calculateValueGain(self):
        return self.value - self.buyPrice
    def gainOrLoss(self):
        return "gain" if self.calculateValueGain() > 0 else "loss"
    @staticmethod
    def loadFromFile(filename:str):
        with open(filename, "rb") as file:
            return pickle.load(file)
    def saveToFile(self, filename:str):
        with open(filename, "wb") as file:
            pickle.dump(self, file)