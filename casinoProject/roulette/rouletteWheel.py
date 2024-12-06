import random

class RouletteWheel:
    def __init__(self):
        self.numbers = list(range(37))
        self.colors = ['green'] + ['red', 'black'] * 18  # 0 is green, rest are red and black

    def spin(self):
        # Randomly select a number from the wheel
        result = random.choice(self.numbers)
        color = self.colors[result]
        return result, color
