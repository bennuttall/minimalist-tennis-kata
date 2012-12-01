class Game:
    point_scores = {
        (0, 0): (15, 0),
        (15, 0): (30, 0),
        (30, 0): (40, 0),
        (40, 0): 'Win',
        (0, 15): (15, 15),
        }

    def __init__(self):
        self.score = (0, 0)

    def get_score(self):
        if type(self.score) is tuple:
            return '%s-%s' % self.score
        return 'Player 1 Wins'

    def point_scored(self, player):
        if player == 1:
            self.score = Game.point_scores[self.score]
        else:
            reversed_score = tuple(reversed(self.score))
            new_score = Game.point_scores[reversed_score]
            self.score = tuple(reversed(new_score))
