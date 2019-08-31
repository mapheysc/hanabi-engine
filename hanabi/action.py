"""Module for Action classes."""

from hanabi.piece import Color
import hanabi.exceptions as exc


class HintAction:
    """Contains information about either a color or a number, but not both."""

    def __init__(self, color=None, number=None):
        """
        Initialize a Hint Action object.

        A hit an be initialized with **either** color or number not both.

        :param color: The color to set the hint. Must be one of the colors on
            Color.COLORS.
        :param number: The number to set the hint. Must be between 1 and 5.
        :raises NoKnownColorException: If the color is not in color.COLORS.
        :raises NoKnownNumberException: If the number is not between 1 and 5.
        """
        if color is not None and number is not None:
            raise exc.HintActionHasColorAndNumber()

        if color in Color.COLORS or color is None:
            self.color = color
        else:
            raise exc.NoKnownColorException(color)

        if number in range(1, 6) or number is None:
            self.number = number
        else:
            raise exc.NoKnownNumberException(number)
