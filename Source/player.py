import pickle
import Source.account as account
import matplotlib.pyplot as plt
import numpy as np
import Source.tax_calculator
import matplotlib

matplotlib.use('Agg') # DO NOT REMOVE, THIS IS NEEDED FOR THREAD-SAFETY

class Player:
    def __init__(self, name:str, startingMoney:float):
        self.name = name
        self.totalMoney = startingMoney
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
        player.stocks = []
        return player

    def makePieChart(self):
        nums = []
        strings = []
        for i in self.accounts:
            if (i.amount > 0):
                nums.append(i.amount)
                strings.append(i.name)
        for i in self.stocks:
            if (i.shares > 0):
                nums.append(i.value)
                strings.append(i.name)
        y = np.array(nums)
        plt.pie(y, labels = strings)
        plt.savefig("static/piechart.png")
        plt.close()

    def makeStockAccount(self, name:str, shares:int, sharePrice:float):
        a = account.StockAccount(name, shares, sharePrice)
        self.stocks.append(a)
    def makeAccount(self, name:str, amount:float):
        a = account.Account(name, amount) # interest is deprecated
        self.accounts.append(a)
    
    def buyShares(self, name:str, amount:int, price:float):
        alreadyBought = False 
        alreadyNegative = False
        for i in self.stocks:
            if i.name == name:
                if not (self.accounts[0].amount - (amount*price) < 0):
                    i.updateShares(amount)
                    alreadyBought = True
                else:
                    alreadyNegative = True
                    break
        if(alreadyNegative == False):
            if  alreadyBought == False:
                self.makeStockAccount(name, amount, price)
            self.accounts[0].amount -= (amount*price)
            
    def sellShares(self, name:str, amount:int, price:float):
        for i in self.stocks:
            if i.name == name:
                i.updateShares(-amount)
                self.accounts[0].amount += (amount*price)

    def calculateTotalMoney(self):
        temp = 0
        for i in self.stocks:
            temp+=i.value
        for i in self.accounts:
            temp+= i.amount
        self.totalMoney = temp

    def transferMoney(self, amount:float, acOne:str, acTwo:str):
        temp1
        temp2
        for i in self.accounts:
            if i.name == acOne:
                temp1 = i
            elif i.name == acTwo:
                temp2 = i
        temp1.removeAmount(amount)
        temp2.addAmount(amount)

    def salaryUpdate(self, salary:int, year:int):
        self.accounts[0].amount += round((salary - Source.tax_calculator.calculate_tax(year, salary))/12,2)
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