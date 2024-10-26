import pickle
import account

class Player:
    def __init__(self, name:str, startingMoney:float):
        self.name = name
        self.money = startingMoney
        self.startingMoney = startingMoney
        self.stocks = 0
        self.accounts = [account.Account("Current Account", startingMoney, 5), account.Account("Savings Account"), 0, 5]
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