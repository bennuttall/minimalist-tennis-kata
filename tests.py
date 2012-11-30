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

if __name__ == '__main__':
    unittest.main()
