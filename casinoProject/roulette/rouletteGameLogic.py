from typing import List
from rouletteWheel import rouletteWheel
from roulettePlayer import roulettePlayer
from rouletteResult import Result
from rouletteBet import rouletteBet

class rouletteGameLogic:
    wheel: rouletteWheel = None
    players: List[roulettePlayer] = None
    bets: List[rouletteBet] = []
    

    def __init__(self, playersAttributes: list):
        self.wheel = rouletteWheel()
        self.players = playersAttributes

    def spinWheel(self) -> Result:
        return self.wheel.spin()
    
    def placeBet(self, playerName: str, betType: str, betValue: str):
        self.bets.append(rouletteBet(playerName, betType, betValue))

    def calculatePayout(self, result: Result):
        roulettePayoutCalculator = roulettePayoutCalculator(self, result, self.bets)
        return self.roulettePayoutCalculator.calculatePayout()
