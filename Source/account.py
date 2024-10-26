import pickle

class Account:
    """
    INTEREST IS DEPRECATED, DO NOT USE
    IT IS VARIABLE, SO IT WILL NOT BE SAVED
    """
    def __init__(self, name:str, amount:float):
        self.name = name
        self.amount = amount
    def updateInterest(self, interest:float): # note, interest should be a monthly interest rate
        amount *= interest/100
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
        self.value = shares*sharePrice
    def updateShares(self, change:int):
        shares += change
        self.calculateValue()
    def updateSharePrice(self, change:int):
        sharePrice += change
        self.calculateValue()
    def calculateValue(self):
        self.value = self.shares* self.sharePrice
    @staticmethod
    def loadFromFile(filename:str):
        with open(filename, "rb") as file:
            return pickle.load(file)
    def saveToFile(self, filename:str):
        with open(filename, "wb") as file:
            pickle.dump(self, file)