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
        (40, 0): 'Win',
        }

    def __init__(self):
        self.score = (0, 0)

    def get_score(self):
        if type(self.score) is tuple:
            return '%s-%s' % self.score
        return 'Player %s Wins' % self.scoring_player

    def point_scored(self, player):
        self.scoring_player = player
        if player == 1:
            self.score = Game.point_scores[self.score]
        else:
            reversed_score = tuple(reversed(self.score))
            new_score = Game.point_scores[reversed_score]
            if type(new_score) is tuple:
                self.score = tuple(reversed(new_score))
            else:
                self.score = new_score
