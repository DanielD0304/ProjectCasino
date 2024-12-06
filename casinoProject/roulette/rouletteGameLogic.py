from typing import List
from rouletteWheel import rouletteWheel
from roulettePlayer import roulettePlayer
from rouletteResult import Result
from rouletteBet import rouletteBet

class rouletteGameLogic:
    bets: List[rouletteBet] = []

    def __init__(self, playersAttributes: list):
        self.wheel = rouletteWheel()
        self.players = playersAttributes

    def spinWheel(self) -> Result:
        return self.wheel.spin()
    
    def placeBet(self, playerID: str, bettingNumbers: set, betAmount: str):
        self.bets.append(rouletteBet(playerID, bettingNumbers, betAmount))

    def calculatePayout(self, result: Result):
        roulettePayoutCalculator = roulettePayoutCalculator(self, result, self.bets)
        return self.roulettePayoutCalculator.calculatePayout()

    def runRoulette(self):
        result = self.spinWheel()
        payout = self.calculatePayout(result)
        for key in payout:
            for player in self.players:
                if player.id == key:
                    player.balance += payout[key]