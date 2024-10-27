import Source.player as player
import Source.account as account

class Goal:
    def __init__(self, name:str, description:str, requiredAmount:int, requiredThreshold:int):
        self.name = name
        self.description = description
        self.requiredAmount = requiredAmount
        self.requiredThreshold = requiredThreshold
        self.amountPaid = 0
        self.completed = False
        self.moneyCounter = account.Account("Goal Account", 0)
    
    def returnResponse(self):
        if(self.amountPaid >= self.requiredAmount):
            self.completed = True
            return True
        else:
            self.completed = False
            return False
        
    def trackAmountPaid(self, amount:int):
        self.amountPaid += amount
    
    def meetsRequirements(self, player:player.Player):
        requirementsMet = False
        if(player.calculateTotalMoney()>=self.requiredThreshold):
            requirementsMet = True
        return requirementsMet