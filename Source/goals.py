import player

class Goal:
    def __init__(self, name:str, description:str, requiredAmount:int, requiredThreshold:int):
        self.name = name
        self.description = description
        self.requiredAmount = requiredAmount
        self.requiredThreshold = requiredThreshold
        self.amountPaid = 0
    
    def returnResponse(self):
        if(self.amountPaid >= self.requiredAmount):
            return f"Congratulations, you have managed to fully purchase a {self.name}"
        else:
            return f"Unfortunuately, you do not have enough to fully purchase a {self.name}. 
            There is still £{self.requiredAmount - self.amountPaid} left to go"
        
    def trackAmountPaid(self, amount:int):
        self.amountPaid += amount
    
    def meetsRequirements(self, player:player.Player):
        requirementsMet = False
        if(player.calculateTotalMoney()>=self.requiredThreshold):
            requirementsMet = True
        return requirementsMet