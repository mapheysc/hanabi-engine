"""Player module for hanabi game."""

from addict import Dict

import hanabi.exceptions as exc
from hanabi.piece import Piece
from hanabi.action import HintAction


class Player:
    """Create a ``Player`` object."""

    def __init__(self, _id, game, name="Anonymous"):
        """
        Initialize a ``Player`` object.

        :param _id: The id to give the player (must be between 0 and 6)
        :param game: The game the the player is a part of.
        :param name: The name of the player.
        """
        self.name = name
        self.id = _id
        self.pieces = []
        self.game = game

    @property
    def dict(self):
        """Convert the ``Player`` object into a dict type."""
        d = Dict()
        d.id = self.id
        d.name = self.name
        d.pieces = [piece.dict for piece in self.pieces]
        return d.to_dict()

    @classmethod
    def from_json(cls, data, game):
        """
        Create an instance of a ``Player`` from a dict and game.

        :param data: The data to create the ``Player`` from.
        :param game: The game to create the ``Player`` with.
        :returns: A new instance of the player.
        """
        player = Dict(data)
        player = cls(data.id, game, name=data.name)
        player.pieces = [Piece.from_json(piece) for piece in data.pieces]
        return player

    def init_pieces(self):
        """Initialize the players pieces."""
        for i in range(4):
            self.pieces.append(self.game.get_random_piece())

    def remove_piece(self, piece):
        """
        Remove a piece from the player.

        :param piece: The piece to remove.
        """
        if not self.game.player_has_turn(self):
            raise exc.NotPlayersTurn(self)
        self.game.turn += 1
        if len(self.pieces) == 0:
            raise exc.TooLittlePiecesError(self)
        else:
            self.pieces.remove(piece)
            self.game.remove_piece(piece)
            self.game.give_piece_to_player(self)
        if len(self.pieces) == 0:
            raise exc.YouLoseGoodDaySir()

    def play_piece(self, piece):
        """
        Play a piece.

        :param piece: The piece to play.
        """
        if not self.game.player_has_turn(self):
            raise exc.NotPlayersTurn(self)
        self.game.turn += 1
        self.game.play_piece(piece)
        self.pieces.remove(piece)
        try:
            self.pieces.append(self.game.get_random_piece())
        except IndexError:
            # Down to the final pieces
            pass
        if len(self.pieces) == 0:
            raise exc.YouLoseGoodDaySir()

    def hint_action_give_color(self, affected_player, color):
        """
        Give a color hint to another player.

        :param affected_player: The player togive the hint to.
        :param color: The color to tell the affected player.
        """
        if not self.game.player_has_turn(self):
            raise exc.NotPlayersTurn(self)
        self.game.turn += 1
        if self.game.num_hints > 0:
            self.game.num_hints -= 1
        else:
            raise exc.HintException()
        affected_player.notify(HintAction(color=color))

    def hint_action_give_number(self, affected_player, number):
        """
        Give a number hint to another player.

        :param affected_player: The player togive the hint to.
        :param number: The number to tell the affected player.
        """
        if not self.game.player_has_turn(self):
            raise exc.NotPlayersTurn(self)
        self.game.turn += 1
        if self.game.num_hints > 0:
            self.game.num_hints -= 1
        else:
            raise exc.HintException()
        affected_player.notify(HintAction(number=number))

    def view_other_players(self):
        """
        View the other players pieces.

        :returns: The other players in the game.
        """
        return [player for player in self.game.players if player != self]

    def view_my_pieces(self):
        """
        View the pieces as the player.

        :returns: The players pieces as viewed by that player.
        """
        return [piece.view_as_self() for piece in self.pieces]

    def notify(self, hint):
        """
        Notify the player that an action has been guven to them.

        :param hint: The hint being given.
        """
        for piece in self.pieces:
            if hint.color == piece.color or piece.color == "rainbow":
                if piece.color == "rainbow":
                    piece.altcolor = hint.color
                piece.player_has_color = True
            elif hint.number == piece.num_fireworks:
                piece.player_has_number = True

    def __repr__(self):
        """Return an unambigous representation of this object."""
        return f"<{self.name} | {self.id} | {self.pieces}>"
