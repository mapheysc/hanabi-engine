from addict import Dict

import hanabi.exceptions as exc
from hanabi.piece import Piece
from hanabi.action import HintAction


class Player:
    def __init__(self, _id, game, name="Anonymous"):
        """Create a player object"""
        self.name = name
        self.id = _id
        self.pieces = []
        self.game = game

    @property
    def dict(self):
        d = Dict()
        d.id = self.id
        d.name = self.name
        d.pieces = [piece.dict for piece in self.pieces]
        return d.to_dict()

    @classmethod
    def from_json(cls, data, game):
        player = Dict(data)
        player = cls(data.id, game, name=data.name)
        player.pieces = [Piece.from_json(piece) for piece in data.pieces]
        return player

    def init_pieces(self):
        for i in range(4):
            self.pieces.append(self.game.get_random_piece())

    def remove_piece(self, piece):
        if not self.game.player_has_turn(self):
            raise exc.NotPlayersTurn(self)
        self.game.turn+=1
        if len(self.pieces) == 0:
            raise exc.TooLittlePiecesError(self)
        else:
            self.pieces.remove(piece)
            self.game.remove_piece(piece)
            self.game.give_piece_to_player(self)
        if len(self.pieces) == 0:
            raise exc.YouLoseGoodDaySir()

    def play_piece(self, piece):
        if not self.game.player_has_turn(self):
            raise exc.NotPlayersTurn(self)
        self.game.turn+=1
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
        if not self.game.player_has_turn(self):
            raise exc.NotPlayersTurn(self)
        self.game.turn+=1
        if self.game.num_hints > 0:
            self.game.num_hints -= 1
        else:
            raise exc.HintException()
        affected_player.notify(HintAction(color=color))

    def hint_action_give_number(self, affected_player, number):
        if not self.game.player_has_turn(self):
            raise exc.NotPlayersTurn(self)
        self.game.turn+=1
        if self.game.num_hints > 0:
            self.game.num_hints -= 1
        else:
            raise exc.HintException()
        affected_player.notify(HintAction(number=number))

    def view_binned_pieces(self):
        return self.game.binned_pieces

    def view_played_pieces(self):
        return self.game.played_pieces

    def view_others_pieces(self):
        return [player for player in self.game.players if player != self]

    def view_my_pieces(self):
        return [piece.view_as_self() for piece in self.pieces]

    def notify(self, action):
        for piece in self.pieces:
            if action.color == piece.color or piece.color == "rainbow":
                if piece.color == "rainbow":
                    piece.altcolor = action.color
                piece.player_has_color = True
            elif action.number == piece.num_fireworks:
                piece.player_has_number = True

    def __repr__(self):
        return f"<{self.name} | {self.id} | {self.pieces}>"
