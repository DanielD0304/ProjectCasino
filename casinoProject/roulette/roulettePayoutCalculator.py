from rouletteBet import rouletteBet

class roulettePayoutCalculator:


    def init (self, bets, result):
        self.bets = bets
        self.result = result

    def calculatePayout(self):
        payouts = {}
        for bet in self.bets:
            if self.result in bet.winning_numbers:
                winningFactor = len(bet.winning_numbers)
                payout = bet.amount * winningFactor
            else:
                payout = 0
            payouts[bet.player_id] = payout
        return payouts
        