class RouletteResult:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def is_even(self):
        return self.number != 0 and self.number % 2 == 0

    def is_odd(self):
        return self.number != 0 and self.number % 2 != 0

    def is_red(self):
        return self.color == 'red'

    def is_black(self):
        return self.color == 'black'

    def is_green(self):
        return self.color == 'green'

    def calculate_payout(self, bet_type, bet_amount):
        if bet_type == 'number' and bet_amount['number'] == self.number:
            return bet_amount['amount'] * 35  # Payout for a straight-up bet is 35:1
        elif bet_type == 'color' and bet_amount['color'] == self.color:
            return bet_amount['amount'] * 2  # Payout for a color bet is 1:1
        elif bet_type == 'even' and self.is_even():
            return bet_amount['amount'] * 2  # Payout for an even bet is 1:1
        elif bet_type == 'odd' and self.is_odd():
            return bet_amount['amount'] * 2  # Payout for an odd bet is 1:1
        else:
            return 0  # No payout if the bet is lost

    def __str__(self):
        return f"Number: {self.number}, Color: {self.color}"