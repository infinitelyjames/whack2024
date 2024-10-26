import pickle

class Account:
    def __init__(self, name:str, amount:float, interest:float):
        self.name = name
        self.amount = amount
        self.interest = interest
    def updateInterest():
        amount *= Account.interest/100
    def addAmount(change:float):
        Account.amount += change
    def removeAmount(change:float):
        Account.addAmount -= change
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
    def updateShares(change:int):
        shares += change
        Account.calculateValue()
    def updateSharePrice(change:int):
        sharePrice += change
        Account.calculateValue()
    def calculateValue():
        value = StockAccount.shares* StockAccount.sharePrice
    @staticmethod
    def loadFromFile(filename:str):
        with open(filename, "rb") as file:
            return pickle.load(file)
    def saveToFile(self, filename:str):
        with open(filename, "wb") as file:
            pickle.dump(self, file)