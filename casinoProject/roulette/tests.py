from django.test import TestCase
from src.rouletteBet import RouletteBet
from src.roulettePayoutCalculator import roulettePayoutCalculator

class RoulettePayoutCalculatorTest(TestCase):

    def test_calculatePayout(self):
        # Erstelle einige Beispielwetten
        bet1 = RouletteBet(player_id=1, winning_numbers={1, 2, 3}, amount=100)
        bet2 = RouletteBet(player_id=2, winning_numbers={4, 5, 6}, amount=200)
        bet3 = RouletteBet(player_id=3, winning_numbers={7, 8, 9}, amount=300)
        
        # Ergebnis der Roulette-Drehung
        result = 2
        
        # Erstelle eine Instanz des PayoutCalculators
        calculator = roulettePayoutCalculator(bets=[bet1, bet2, bet3], result=result)
        
        # Berechne die Auszahlungen
        payouts = calculator.calculatePayout()
        
        # Überprüfe die Auszahlungen
        self.assertEqual(payouts[1], 300)  # bet1 gewinnt, da 2 in winning_numbers ist (100 * 3)
        self.assertEqual(payouts[2], 0)    # bet2 verliert, da 2 nicht in winning_numbers ist
        self.assertEqual(payouts[3], 0)