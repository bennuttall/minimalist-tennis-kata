from tennis import *
import unittest


class Test(unittest.TestCase):
    def test_score_of_new_game_is_0_0(self):
        game = Game()
        self.assertEqual(game.get_score(), '0-0')

    def test_player_one_scores_point_score_is_15_0(self):
        game = Game()
        game.point_scored(1)
        self.assertEqual(game.get_score(), '15-0')

    def test_player_one_scores_two_points_score_is_30_0(self):
        game = Game()
        game.point_scored(1)
        game.point_scored(1)
        self.assertEqual(game.get_score(), '30-0')

    def test_player_one_scores_three_points_score_is_40_0(self):
        game = Game()
        game.point_scored(1)
        game.point_scored(1)
        game.point_scored(1)
        self.assertEqual(game.get_score(), '40-0')

    def test_player_one_scores_four_points_player_one_wins(self):
        game = Game()
        game.point_scored(1)
        game.point_scored(1)
        game.point_scored(1)
        game.point_scored(1)
        self.assertEqual(game.get_score(), 'Player 1 Wins')

if __name__ == '__main__':
    unittest.main()
