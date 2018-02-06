from application.GameBoard import GameBoard
import itertools
flatten = itertools.chain.from_iterable



def test_init_board_from_string():
    string="r e b w r b b b r r r b r b w"
    game_board=GameBoard(string)
    flattened_string=''.join(list(flatten(game_board.board)))
    assert(flattened_string==string.replace(" ",""))
