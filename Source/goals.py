import Source.player as player

class Goal:
    def __init__(self, name:str, description:str, requiredAmount:int, requiredThreshold:int):
        self.name = name
        self.description = description
        self.requiredAmount = requiredAmount
        self.requiredThreshold = requiredThreshold
        self.amountPaid = 0
        self.completed = False
    
    def returnResponse(self):
        if(self.amountPaid >= self.requiredAmount):
            self.completed = True
            return True
            #return f"Congratulations, you have managed to fully purchase a {self.name}"
        else:
            self.completed = False
            return False#f"Unfortunuately, you do not have enough to fully purchase a {self.name}. There is still £{self.requiredAmount - self.amountPaid} left to go"
        
    def trackAmountPaid(self, amount:int):
        self.amountPaid += amount
    
    def meetsRequirements(self, player:player.Player):
        requirementsMet = False
        if(player.calculateTotalMoney()>=self.requiredThreshold):
            requirementsMet = True
        return requirementsMet