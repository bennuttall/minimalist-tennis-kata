class Game:
    point_scores = {
        (0, 0): (15, 0),
        (0, 15): (15, 15),
        (0, 30): (15, 30),
        (0, 40): (15, 40),
        (15, 0): (30, 0),
        (15, 15): (30, 15),
        (15, 30): (30, 30),
        (15, 40): (30, 40),
        (30, 0): (40, 0),
        (30, 15): (40, 15),
        (30, 30): (40, 30),
        (30, 40): 'Deuce',
        (40, 0): 'Win',
        (40, 15): 'Win',
        (40, 30): 'Win',
        'Deuce': 'Advantage',
        }

    def __init__(self):
        self.score = (0, 0)

    def get_score(self):
        if type(self.score) is tuple:
            return '%s-%s' % self.score
        return self.score

    def point_scored(self, player):
        if player == 1:
            self.score = Game.point_scores[self.score]
        else:
            reversed_score = tuple(reversed(self.score))
            self.score = Game.point_scores[reversed_score]
            if type(self.score) is tuple:
                self.score = tuple(reversed(self.score))
        if type(self.score) is str:
            self.score = self.string_score(player)

    def string_score(self, player):
        if self.score == 'Advantage':
            return 'Advantage Player %s' % player
        elif self.score == 'Win':
            return 'Player %s Wins' % player
        return 'Deuce'
