import pickle

class Player:
    def __init__(self, name:str, startingMoney:float):
        self.name = name
        self.money = startingMoney
        self.startingMoney = startingMoney
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