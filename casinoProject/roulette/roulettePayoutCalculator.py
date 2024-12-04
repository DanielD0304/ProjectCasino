from rouletteBet import rouletteBet

class roulettePayoutCalculator:


    def init (self, bets, result):
        self.bets = bets
        self.result = result

    def calculatePayout(self):
        # Initialisiere das payouts Dictionary mit allen Spielern und einem Payout von 0
        payouts = {bet.player_id: 0 for bet in self.bets}
        # Berechne die Auszahlungen für jede Wette
        for bet in self.bets:
            if self.result in bet.winning_numbers:
                winningFactor = 36/len(bet.winning_numbers)
                payout = bet.amount * winningFactor
            else:
                payout = 0
            payouts[bet.player_id] += payout
            
        return payouts
        