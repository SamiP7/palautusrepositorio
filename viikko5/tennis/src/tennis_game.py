class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.scores_equal():
            return self.scores_equal()
        elif self.match_point():
            return self.match_point()

        return f'{self.return_score(self.player1_score)}-{self.return_score(self.player2_score)}'



    def scores_equal(self):
        if self.player1_score == self.player2_score:
            if self.player1_score == 0:
                return "Love-All"
            elif self.player1_score == 1:
                return "Fifteen-All"
            elif self.player1_score == 2:
                return "Thirty-All"
            elif self.player1_score == 3:
                return "Forty-All"
            else:
                return "Deuce"
        return None

    def match_point(self):
        if self.player1_score >= 4 or self.player2_score >= 4:
            advantage = self.player1_score - self. player2_score
            if advantage == 1:
                return "Advantage player1"
            if advantage >= 2:
                return "Win for player1"
            if advantage == -1:
                return "Advantage player2"
            if advantage <= -2:
                return "Win for player2"
        return None

    def return_score(self, score):
        if (score == 0):
            return "Love"
        if (score == 1):
            return "Fifteen"
        if (score == 2):
            return "Thirty"
        return "Forty"