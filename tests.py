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

    def test_player_one_scores_then_player_two_scores_score_is_15_15(self):
        game = Game()
        game.point_scored(1)
        game.point_scored(2)
        self.assertEqual(game.get_score(), '15-15')

    def test_player_two_scores_score_is_0_15(self):
        game = Game()
        game.point_scored(2)
        self.assertEqual(game.get_score(), '0-15')

    def test_player_two_scores_twice_score_is_0_30(self):
        game = Game()
        game.point_scored(2)
        game.point_scored(2)
        self.assertEqual(game.get_score(), '0-30')

    def test_one_scores_twice_and_player_two_scores_twice_score_is_30_30(self):
        game = Game()
        game.point_scored(1)
        game.point_scored(1)
        game.point_scored(2)
        game.point_scored(2)
        self.assertEqual(game.get_score(), '30-30')

if __name__ == '__main__':
    unittest.main()
