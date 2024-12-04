
class roulettePlayer:


    def __init__(self, playerName: str, playerBalance: int, playerID: int):
        self.playerName = playerName
        self.playerBalance = playerBalance
        self.playerID = playerID

    def get_balance(self):
        return self.playerBalance

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

    #Je nachdem ob wir bets in gamelogic implementieren wollen oder hier
    def place_bet(self, amount: int, bet_type: str):
        self.subtract_balance(amount)
        return {"amount": amount, "bet_type": bet_type}

