import pickle
import account
import matplotlib.pyplot as plt
import numpy as np

class Player:
    accounts = []
    stocks = []
    def __init__(self, name:str, startingMoney:float):
        self.name = name
        self.money = startingMoney
        self.startingMoney = startingMoney
        self.stocks = 0
        Player.makeAccount("Current Account", startingMoney, 5)
        Player.makeAccount("Savings Account", 0, 5)

    def makePieChart():
        nums = []
        strings = []
        for i in Player.accounts:
            nums.append(i.amount)
            strings.append(i.name)
        for i in Player.stocks:
            nums.append(i.amount)
            strings.append(i.name)
        y = np.array(nums)
        plt.pie(y, labels = strings)
        plt.savefig("static/piechart.png")

    def makeStockAccount(name:str, shares:int, sharePrice:float):
        a = account.Account((name, shares, sharePrice))
        Player.stocks.append(a)
    def makeAccount(name:str, amount:float, interest:float):
        a = account.Account((name, amount, interest))
        Player.accounts.append(a)
    @staticmethod
    def loadDefaultPlayer(name="Default player"):
        return Player(name, 1000)
    @staticmethod
    def loadFromFile(filename:str):
        with open(filename, "rb") as file:
            return pickle.load(file)
    def saveToFile(self, filename:str):
        with open(filename, "wb") as file:
            pickle.dump(self, file)