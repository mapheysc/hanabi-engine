from hanabi.piece import Color
import hanabi.exceptions as exc

class Action:

    def __init__(self, performing_player):
        self.performing_player = performing_player

class HintAction:

    def __init__(self, color=None, number=None):
        if color in Color.COLORS or color is None:
            self.color = color
        else:
            raise exc.NoKnownColorException(color)

        if number in range(1, 6) or number is None:
             self.number = number
        else:
            raise exc.NoKnownNumberException(number)