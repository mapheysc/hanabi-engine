"""Contains exception definitions used throughout hanabi."""


class TooManyPiecesError(Exception):
    """Player has too many pieces."""

    def __init__(self, player):
        """
        Initialize an ``TooManyPiecesError`` exception.

        :param player: The player who had too many pieces.
        """
        self.message = "Player " + str(player) + " has too many pieces."
        self.player = player

    def __str__(self):
        """User friendly representation of a ``TooManyPiecesError`` object."""
        return self.message


class TooLittlePiecesError(Exception):
    """Player has too lttle pieces."""

    def __init__(self, player):
        """
        Initialize an ``TooLittlePiecesError`` exception.

        :param player: The player who had too little pieces.
        """
        self.message = "Player " + str(player) + " does not have enough pieces."
        self.player = player

    def __str__(self):
        """User friendly representation of a ``TooLittlePiecesError`` object."""
        return self.message


class YouLoseGoodDaySir(Exception):
    """Game has been lost."""

    def __init__(self):
        """Initialize an ``YouLoseGoodDaySir`` exception."""
        self.message = "Opps too bad. You lost."

    def __str__(self):
        """User friendly representation of a ``YouLoseGoodDaySir`` object."""
        return self.message


class HintException(Exception):
    """Not enough hints to give."""

    def __init__(self):
        """Initialize an ``HintException`` exception."""
        self.message = f"Not enough hints to give."

    def __str__(self):
        """User friendly representation of a ``HintException`` object."""
        return self.message


class NoKnownColorException(Exception):
    """Color is not recognized."""

    def __init__(self, color):
        """
        Initialize an ``NoKnownColorException`` exception.

        :param color: The color used.
        """
        self.message = f"Color {color} is not a known color."

    def __str__(self):
        """User friendly representation of a ``NoKnownColorException`` object."""
        return self.message


class NoKnownNumberException(Exception):
    """Number is not recognized."""

    def __init__(self, number):
        """
        Initialize an ``NoKnownNumberException`` exception.

        :param number: The number used.
        """
        self.message = f"Number {number} is not a known number."

    def __str__(self):
        """User friendly representation of a ``NoKnownNumberException`` object."""
        return self.message


class NotPlayersTurn(Exception):
    """Not players turn."""

    def __init__(self, player):
        """
        Initialize an ``NotPlayersTurn`` exception.
        
        :param player: The player who tried to play.
        """
        self.message = f"Player {player} does not have turn."

    def __str__(self):
        """User friendly representation of a ``NotPlayersTurn`` object."""
        return self.message


class HintActionHasColorAndNumber(Exception):
    """Hint action uses both color and number."""

    def __init__(self):
        """Initialize an ``HintActionHasColorAndNumber`` exception."""
        self.message = f"Cannot create hint action with color and number."

    def __str__(self):
        """User friendly representation of a ``HintActionHasColorAndNumber`` object."""
        return self.message
