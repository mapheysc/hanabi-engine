class TooManyPiecesError(Exception):
    def __init__(self, player):
        self.message = "Player " + str(player) + " has too many pieces."
        self.player = player

    def __str__(self):
        return self.message

    def __repr__(self):
        return f"<{self.player}>"


class TooLittlePiecesError(Exception):
    def __init__(self, player):
        self.message = "Player " + str(player) + " does not have enough pieces."
        self.player = player

    def __str__(self):
        return self.message

    def __repr__(self):
        return f"<{self.player}>"


class YouLoseGoodDaySir(Exception):
    def __init__(self):
        self.message = "Opps too bad. You lost."

    def __str__(self):
        return self.message


class HintException(Exception):
    def __init__(self):
        self.message = f"Not enough hints to give."

    def __str__(self):
        return self.message


class NoKnownColorException(Exception):
    def __init__(self, color):
        self.message = f"Color {color} is not a known color."

    def __str__(self):
        return self.message


class NoKnownNumberException(Exception):
    def __init__(self, number):
        self.message = f"Number {number} is not a known number."

    def __str__(self):
        return self.message


class NotPlayersTurn(Exception):
    def __init__(self, player):
        self.message = f"Player {player.id} does not have turn."

    def __str__(self):
        return self.message
