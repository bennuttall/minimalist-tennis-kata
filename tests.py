from tennis import *
import unittest

class Test(unittest.TestCase):
    def test_score_of_new_game_is_0_0(self):
        game = Game()
        self.assertEqual(game.get_score(), '0-0')

if __name__ == '__main__':
    unittest.main()
