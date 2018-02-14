from application.GameBoard import GameBoard
import itertools
flatten = itertools.chain.from_iterable



def test_init_board_from_string():
    string="r e b w r b b b r r r b r b w"
    game_board=GameBoard(string)
    flattened_string=''.join(list(flatten(game_board.board)))
    assert(flattened_string==string.replace(" ",""))

def test_check_failed_goal_state():
    string = "b b r e w w b b r r b b r r r"
    game_board = GameBoard(string)
    assert(False == game_board.check_goal_state())

def test_check_succesfull_goal_state():
    string = "r e b w r b b b r r r e b w r"
    game_board = GameBoard(string)
    assert(True == game_board.check_goal_state())