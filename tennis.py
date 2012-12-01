class Game:
    point_scores = {
        (0, 0): (15, 0),
        (15, 0): (30, 0),
        }

    def __init__(self):
        self.score = (0, 0)

    def get_score(self):
        return '%s-%s' % self.score

    def point_scored(self, player):
        self.score = Game.point_scores[self.score]
