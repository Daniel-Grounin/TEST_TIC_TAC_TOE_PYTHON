import unittest
import Tic_Tac_Toe

if __name__ == '__main__':
    unittest.main()

class TestTicTacToe(unittest.TestCase):

    def test_is_valid_move_returns_true_if_move_is_valid(self):
        Tic_Tac_Toe.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertTrue(Tic_Tac_Toe.is_valid_move(0, 0, Tic_Tac_Toe.CROSS), "CROSS is valid")
        self.assertTrue(Tic_Tac_Toe.is_valid_move(1, 0, Tic_Tac_Toe.CROSS), "CROSS is valid")
        self.assertTrue(Tic_Tac_Toe.is_valid_move(1, 1, Tic_Tac_Toe.CROSS), "CROSS is valid")
        self.assertFalse(Tic_Tac_Toe.is_valid_move(1, 1, Tic_Tac_Toe.CIRCLE), "CROSS is invalid") #Unable to place a circle on top of a cross
        self.assertTrue(Tic_Tac_Toe.is_valid_move(1, 2, Tic_Tac_Toe.CIRCLE), "CIRCLE is valid")
        self.assertTrue(Tic_Tac_Toe.is_valid_move(2, 1, Tic_Tac_Toe.CIRCLE), "CIRCLE is valid")


    def test_has_won_returns_true_if_player_has_won(self):
        Tic_Tac_Toe.board = [[1, 1, 1], [0, 2, 0], [0, 0, 2]]
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 0), "CROSS has won")
        Tic_Tac_Toe.board = [[0, 2, 0], [1, 1, 1], [0, 0, 2]]
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 1, 0), "CROSS has won")
        Tic_Tac_Toe.board = [[2, 0, 1], [0, 0, 1], [0, 2, 1]]
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 0, 2), "CROSS has won")
        Tic_Tac_Toe.board = [[2, 0, 1], [0, 0, 2], [1, 1, 1]]
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CROSS, 2, 0), "CROSS has won")
        Tic_Tac_Toe.board = [[0, 2, 0], [0, 2, 0], [2, 2, 2]]
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 0, 1), "CIRCLE has won")
        Tic_Tac_Toe.board = [[2, 2, 2], [0, 1, 0], [0, 0, 1]]
        self.assertTrue(Tic_Tac_Toe.has_won(Tic_Tac_Toe.CIRCLE, 0, 0), "CIRCLE has won")

    def test_validate_3_in_diagonal_returns_true_if_3_in_diagonal(self):
        Tic_Tac_Toe.board = [[1, 0, 2], [0, 1, 0], [2, 0, 1]]
        self.assertTrue(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CROSS), "CROSS has won")
        Tic_Tac_Toe.board = [[2, 0, 0], [1, 2, 0], [1, 0, 2]]
        self.assertTrue(Tic_Tac_Toe.validate_3_in_diagonal(Tic_Tac_Toe.CIRCLE), "CIRCLE has won")

    def test_backward_diagonal_returns_true_if_3_in_backward_diagonal(self):
        Tic_Tac_Toe.board = [[0, 0, 2], [1, 2, 0], [2, 0, 1]]
        self.assertTrue(Tic_Tac_Toe.backward_diagonal(Tic_Tac_Toe.CIRCLE), "CIRCLE has won")
        Tic_Tac_Toe.board = [[0, 0, 1], [2, 1, 0], [1, 0, 2]]
        self.assertTrue(Tic_Tac_Toe.backward_diagonal(Tic_Tac_Toe.CROSS), "CROSS has won")

    def test_forward_diagonal_returns_true_if_3_in_forward_diagonal(self):
        Tic_Tac_Toe.board = [[2, 0, 1], [1, 2, 0], [1, 0, 2]]
        self.assertTrue(Tic_Tac_Toe.forward_diagonal(Tic_Tac_Toe.CIRCLE), "CIRCLE has won")
        Tic_Tac_Toe.board = [[1, 0, 2], [0, 1, 0], [0, 2, 1]]
        self.assertTrue(Tic_Tac_Toe.forward_diagonal(Tic_Tac_Toe.CROSS), "CROSS has won")

    def test_validate_3_in_column_returns_true_if_3_in_column(self):
        Tic_Tac_Toe.board = [[2, 0, 1], [2, 1, 0], [2, 0, 0]]
        self.assertTrue(Tic_Tac_Toe.validate_3_in_column(0, Tic_Tac_Toe.CIRCLE), "CIRCLE has won")
        Tic_Tac_Toe.board = [[1, 0, 2], [1, 0, 0], [1, 2, 0]]
        self.assertTrue(Tic_Tac_Toe.validate_3_in_column(0, Tic_Tac_Toe.CROSS), "CROSS has won")

    def test_3_in_row_returns_true_if_3_in_row(self):
        Tic_Tac_Toe.board = [[2, 2, 2], [0, 1, 0], [1, 0, 0]]
        self.assertTrue(Tic_Tac_Toe.validate_3_in_row(0, Tic_Tac_Toe.CIRCLE), "CIRCLE has won")
        Tic_Tac_Toe.board = [[1, 1, 1], [0, 0, 0], [2, 2, 0]]
        self.assertTrue(Tic_Tac_Toe.validate_3_in_row(0, Tic_Tac_Toe.CROSS), "CROSS has won")
