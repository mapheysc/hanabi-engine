"""Game handler for hanabi."""

import itertools as it

from random import randint
from addict import Dict

import hanabi.exceptions as exc
from hanabi.player import Player
from hanabi.piece import Color, Piece


def init_pieces():
    """
    Initialize pieces for the game.

    Creates 5 or 6 (game is played with rainbows) sets of 10 color pieces.
    Each set has 3 ones,  2 twos, 2 threes, 2 fours, and 1 five.
    """
    pieces = []
    for color in Color.COLORS:
        for num_fireworks in range(1, 6):
            if num_fireworks == 1:
                # 3 fireworks with value of 1
                pieces.append(
                    Piece(num_fireworks=num_fireworks, color=color)
                )
                pieces.append(
                    Piece(num_fireworks=num_fireworks, color=color)
                )
                pieces.append(
                    Piece(num_fireworks=num_fireworks, color=color)
                )
            elif num_fireworks == 5:
                # 1 firework with value of 5
                pieces.append(
                    Piece(num_fireworks=num_fireworks, color=color)
                )
            else:
                # 2 firework with value of anything other than 1 and 5
                pieces.append(
                    Piece(num_fireworks=num_fireworks, color=color)
                )
                pieces.append(
                    Piece(num_fireworks=num_fireworks, color=color)
                )
    return pieces


class Game:
    """Create a ``Game`` object."""

    def __init__(
        self,
        num_players,
        with_rainbows=False,
        name=None,
        num_hints=8,
        num_errors=4,
        turn=0
    ):
        """
        Initialize a ``Game`` object.

        :param num_players: The number of players to play with.
        :param with_rainbows: Whether or not to play the game with rainbows.
        :param name: The games name.
        :param num_hints: The number of hints to initialize the game with.
        :param num_errors: The number of error to initialize the game with.
        :param turn: The player id to start the game with.
        """
        self.available_pieces = init_pieces()
        self.binned_pieces = []
        self.played_pieces = []
        self.num_hints = num_hints
        self.num_errors = num_errors
        self.with_rainbows = with_rainbows
        self.players = [Player(i, self) for i in range(num_players)]
        self.name = name
        if self.with_rainbows:
            Color.COLORS.append("rainbow")
        self.turn = turn
        self.has_finished = False

    @property
    def dict(self):
        """Convert the Game object into a dict type."""
        game_state = Dict()
        game_state.players = [player.dict for player in self.players]
        game_state.available_pieces = [piece.dict for piece in self.available_pieces]
        game_state.binned_pieces = [piece.dict for piece in self.binned_pieces]
        game_state.played_pieces = [piece.dict for piece in self.played_pieces]
        game_state.num_hints = self.num_hints
        game_state.num_errors = self.num_errors
        game_state.with_rainbows = self.with_rainbows
        game_state.name = self.name
        game_state.turn = self.turn
        if self.num_errors == 0:
            raise exc.YouLoseGoodDaySir()
        return game_state.to_dict()

    @classmethod
    def from_json(cls, data):
        """
        Create an instance of a ``Game`` from a dict.

        :param data: The data to create the Game from.
        :returns: A new instance of the game.
        """
        game = Dict(data)
        game = cls(
            num_players=len(data.players),
            with_rainbows=data.with_rainbows,
            num_hints=int(data.num_hints),
            num_errors=int(data.num_errors),
            name=data.name,
            turn=data.turn
        )
        game.available_pieces = [
            Piece.from_json(piece) for piece in data.available_pieces
        ]
        game.binned_pieces = [Piece.from_json(piece) for piece in data.binned_pieces]
        game.played_pieces = [Piece.from_json(piece) for piece in data.played_pieces]
        game.players = [Player.from_json(player, game) for player in data.players]
        if int(data.num_errors) == 0:
            raise exc.YouLoseGoodDaySir()
        return game

    def player_has_turn(self, player):
        """
        Check to see if it is the players turn.

        :param player: The player to check against.
        :returns: True if it is the players turn. False otherwise.
        """
        return True if self.turn % len(self.players) == player.id else False

    def get_piece(self, piece_id):
        """
        Get a piece object from a given id.

        :param piece_id: The id of the piece.
        :returns: The piece if found in the games pieces.
        """
        player_pieces = list(
            it.chain.from_iterable([player.pieces for player in self.players])
        )
        pieces = (
            self.played_pieces
            + self.binned_pieces
            + self.available_pieces
            + player_pieces
        )
        return next(p for p in pieces if p.id == piece_id)

    def start_game(self):
        """Start the game."""
        for player in self.players:
            player.init_pieces()

    def give_piece_to_player(self, player):
        """
        Give a random piece to a player.

        :param player: The player to gice the piece to.
        """
        player.pieces.append(self.get_random_piece())

    def get_random_piece(self):
        """Get a random piece from the list of available pieces."""
        piece = self.available_pieces[randint(0, len(self.available_pieces)) - 1]
        self.available_pieces.remove(piece)
        return piece

    def remove_piece(self, piece):
        """
        Remove a piece.

        Increases the number of hints by one.
        Adds the piece to the list of binned pieces.
        Removes the piece from the list of available pieces.
        :param piece: The piece to remove
        """
        self.binned_pieces.append(piece)
        self.available_pieces.remove(piece)
        self.num_hints += 1

    def piece_can_be_played(self, piece):
        """
        Check to see if the piece can be played.

        :param piece: The piece to check.
        :returns: True:
                If the piece's number of fireworks is one more
                than another piece in the list of played pieces or the number
                of fireworks is one and played pieces has less than 5 ones.
            False: Otherwise.
        """
        for p in self.played_pieces:
            if p == piece:
                raise Exception("I have no idea how this happened.")
            if p.color == piece.color:
                if p.num_fireworks == piece.num_fireworks - 1:
                    return True
                elif p.num_fireworks == piece.num_fireworks:
                    return False
        if piece.num_fireworks == 1:
            if len([_ for _ in self.available_pieces if p.num_fireworks == 1] < 5):
                return True
        return False

    def play_piece(self, piece):
        """
        Play a piece.

        Checks if the piece can be played.
            If the piece can be played then it removes the piece from the
            list of available pieces. Appends the piece to the list of played pieces.

            If the piece has 5 fireworks then gives the game another hint.

        If the piece cannot be played.
            Adds the piece to the list of binned pieces.
            Removes the piece from the list of available pieces.
            Decreases the number of  errors.
            If the number of errors is 0 then finish the game.
        :param piece: The piece to be played.
        """
        if self.piece_can_be_played(piece):
            self.available_pieces.remove(piece)
            self.played_pieces.append(piece)
            if piece.num_fireworks == 5:
                if self.num_hints < 8:
                    self.num_hints += 1
        else:
            self.binned_pieces.append(piece)
            self.available_pieces.remove(piece)
            self.num_errors -= 1
            if self.num_errors == 0:
                self.has_finished = True
                raise exc.YouLoseGoodDaySir()
