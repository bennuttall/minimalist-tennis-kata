class Game:
    def __init__(self):
        self.score = (0, 0)

    def get_score(self):
        return '%s-%s' % (self.score[0], self.score[1])

    def point_scored(self, player):
        self.score = (15, 0)
