import pickle
import Source.account as account
import matplotlib.pyplot as plt
import numpy as np

class Player:
    def __init__(self, name:str, startingMoney:float):
        self.name = name
        self.money = startingMoney
        self.startingMoney = startingMoney
        self.accounts = []
        self.stocks = []
        self.makeAccount("Current Account", startingMoney)
        self.makeAccount("Savings Account", 0)
    
    @staticmethod
    def loadDefaultPlayer(name="John"):
        player = Player(name, 10000)
        player.accounts = [
            account.Account("Current Account", 1100),
            account.Account("Savings Account", 500)
        ]
        player.stockAccounts = [
            account.StockAccount("Apple", 10, 100),
        ]
        return player

    def makePieChart(self):
        nums = []
        strings = []
        for i in self.accounts:
            if (i.amount > 0):
                nums.append(i.amount)
                strings.append(i.name)
        for i in self.stocks:
            if (i.amount > 0):
                nums.append(i.amount)
                strings.append(i.name)
        y = np.array(nums)
        plt.pie(y, labels = strings)
        plt.savefig("static/piechart.png")

    def makeStockAccount(self, name:str, shares:int, sharePrice:float):
        a = account.StockAccount(name, shares, sharePrice)
        self.stocks.append(a)
    def makeAccount(self, name:str, amount:float):
        a = account.Account(name, amount) # interest is deprecated
        self.accounts.append(a)
    
    def buyShares(self, name:str, amount:int, price:float):
        alreadyBought = False 
        for i in self.stocks:
            if i.name == name:
                i.shares += amount
                alreadyBought = True
        if not alreadyBought:
            self.makeStockAccount(name, amount, price)
        self.money -= (amount*price)
            
    def sellShares(self, name:str, amount:int, price:float):
        for i in self.stocks:
            if i.name == name:
                i.shares -= amount
                self.money += (amount*price)


    def salaryUpdate(self, salary:int, taxes:float):
        self.accounts[0].amount += (salary*taxes/100)
    @staticmethod
    def loadFromFile(filename:str):
        with open(filename, "rb") as file:
            return pickle.load(file)
    def saveToFile(self, filename:str):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

def main():
    player = Player("John", 10000)
    player.makePieChart()

if __name__ == "__main__":
    main()