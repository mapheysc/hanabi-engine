"""Piece module for hanabi game."""

from addict import Dict
import uuid


class Piece:
    """Create a ``Piece`` object."""

    def __init__(
        self, num_fireworks, color, player_has_color=False, player_has_number=False
    ):
        """
        Initialize a ``Piece`` object.

        :param num_firworks: The number of fireworks to give the piece
            (accepted values are 1 - 5)
        :param color: The color to gievthe piece. Accepted values can be
            found in Color.COLORS.
        :param player_has_color: Whether or not the player knows the color.
        :param player_has_number: Whether or not the player knows the number.
        """
        self.num_fireworks = num_fireworks
        self.color = color
        self.altcolor = ""
        self.player_has_color = player_has_color
        self.player_has_number = player_has_number
        self.id = str(uuid.uuid4())

    @property
    def dict(self):
        """Convert the ``Piece`` object into a dict type."""
        d = Dict()
        d.num_fireworks = self.num_fireworks
        d.color = self.color
        d.altcolor = self.altcolor
        d.player_has_color = self.player_has_color
        d.player_has_number = self.player_has_number
        d.id = self.id
        return d.to_dict()

    @classmethod
    def from_json(cls, data):
        """
        Create an instance of a ``Piece`` from a dict.

        :param data: The data to create the ``Piece`` from.
        :returns: A new instance of the piece.
        """
        piece = Dict(data)
        piece = cls(
            num_fireworks=data.num_fireworks,
            color=data.color,
            player_has_color=data.player_has_color,
            player_has_number=data.player_has_number,
        )
        piece.id = data.id
        return piece

    def view_as_self(self):
        """
        View the piece as a player.

        If the player knows the number then show the number. Otherwise show *.
        If the player knows the color then show the color. Otherwise show *.
        """
        color = "*"
        num_fireworks = "*"
        if self.player_has_color:
            if self.color != "rainbow":
                color = self.color
            else:
                if self.altcolor is not None:
                    color = self.altcolor
        if self.player_has_number:
            num_fireworks = self.num_fireworks
        return f"<{color} | {num_fireworks}>"

    def __repr__(self):
        """Return an unambigous representation of this object."""
        return f"<{self.color} | {self.num_fireworks} | " \
            f"player_has_color={self.player_has_color} | " \
            f"player_has_number={self.player_has_number}>"


class Color:
    """Define a list of acceptable colors."""

    COLORS = ["red", "white", "blue", "green", "yellow"]
