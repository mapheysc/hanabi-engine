"""Module for Action classes."""

from hanabi.piece import Color
import hanabi.exceptions as exc


class HintAction:
    """Contains information about either a color or a number, but not both."""

    def __init__(self, color=None, number=None):
        if color in Color.COLORS or color is None:
            self.color = color
        else:
            raise exc.NoKnownColorException(color)

        if number in range(1, 6) or number is None:
            self.number = number
        else:
            raise exc.NoKnownNumberException(number)
