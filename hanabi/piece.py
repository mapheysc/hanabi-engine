from addict import Dict
import uuid


class Piece:
    def __init__(
        self, num_fireworks, color, player_has_color=False, player_has_number=False
    ):
        """Create a piece."""
        self.num_fireworks = num_fireworks
        self.color = color
        self.altcolor = ""
        self.player_has_color = player_has_color
        self.player_has_number = player_has_number
        self.id = str(uuid.uuid4())

    @property
    def dict(self):
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
        return f"<{self.color} | {self.num_fireworks} | " \
            f"player_has_color={self.player_has_color} | " \
            f"player_has_number={self.player_has_number}>"


class Color:
    COLORS = ["red", "white", "blue", "green", "yellow"]
