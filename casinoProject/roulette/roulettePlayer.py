
class roulettePlayer:


    def __init__(self, playerName: str, playerBalance: int, playerID: int):
        self.playerName = playerName
        self.playerBalance = playerBalance
        self.playerID = playerID

    def get_balance(self):
        return self.playerBalance
    
    def get_name(self):
        return self.playerName
    
    def get_id(self):
        return self.playerID

    def add_balance(self, amount: int):
        if amount < 0:
            #Wäre besser wenn wir es vor dem Aufrufen im PayoutCalculator überprüfen
            raise ValueError("Amount to add should be positive")
        self.playerBalance += amount
    
     
    def subtract_balance(self, amount: int):
        if amount < 0:
            raise ValueError("Amount to subtract should be positive")
        elif self.playerBalance < amount:
            raise ValueError("Not enough balance")
        self.playerBalance -= amount
