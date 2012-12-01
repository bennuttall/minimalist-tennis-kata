class Game:
    point_scores = {
        (0, 0): (15, 0),
        (15, 0): (30, 0),
        (30, 0): (40, 0),
        (40, 0): 'Win',
        }

    def __init__(self):
        self.score = (0, 0)

    def get_score(self):
        if type(self.score) is tuple:
            return '%s-%s' % self.score
        return 'Player 1 Wins'

    def point_scored(self, player):
        self.score = Game.point_scores[self.score]
