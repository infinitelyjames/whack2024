import pickle

class Account:
    def __init__(self, name:str, amount:float, interest:float):
        self.name = name
        self.amount = amount
        self.interest = interest
    def updateInterest(self):
        amount *= self.interest/100
    def addAmount(self, change:float):
        self.amount += change
    def removeAmount(self, change:float):
        self.addAmount -= change
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
        value = shares*sharePrice
    def updateShares(self, change:int):
        shares += change
        self.calculateValue()
    def updateSharePrice(self, change:int):
        sharePrice += change
        self.calculateValue()
    def calculateValue(self):
        value = self.shares* self.sharePrice
    @staticmethod
    def loadFromFile(filename:str):
        with open(filename, "rb") as file:
            return pickle.load(file)
    def saveToFile(self, filename:str):
        with open(filename, "wb") as file:
            pickle.dump(self, file)