# Hanabi Game Engine

## Building the game engine locally

- clone the repo

## Install Requirements

**Build a vitrual environment if you wish (highly reccommended)**
`python -m venv hanabi`

`cd hanabi-engine && pip install -r requirements.txt`

## Documentation

[Here (not hosted yet)](google.com)

## Examples

### Building a game

```python
from hanabi.game import Game

game = Game(num_players=3, with_rainbows=False)

player_1 = game.players[0]
player_2 = game.players[1]
player_3 = game.players[2]

player_1.hint_action_give_color(player_2, 'yellow')

print(player_2.view_my_pieces())

piece_to_play = next(piece for piece in player_2.pieces if piece.color == 'yellow')
player_2.play_piece(piece_to_play)

piece_to_remove = player_1.pieces[0]
player_1.remove_piece(piece_to_remove)
```
