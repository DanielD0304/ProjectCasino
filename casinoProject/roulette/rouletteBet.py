class RouletteBet:
    def __init__(self, player_id: str, betting_numbers: set, amount: int):
        self.player_id = player_id
        self.betting_numbers = betting_numbers
        self.amount = amount

    def __repr__(self):
        return f"RouletteBet(player_id={self.player_id}, winning_numbers={self.winning_numbers}, amount={self.amount})"