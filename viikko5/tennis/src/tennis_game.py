class TennisGame:
    POINTS_TO_SCORE = {
        0: "Love",
        1: "Fifteen", 
        2: "Thirty",
        3: "Forty"
    }

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

    def victory(self):
        return self.player1_score >= 4 or self.player2_score >= 4
    
    def get_score(self):
        if self.player1_score == self.player2_score:
            if self.player1_score >= 3:
                return "Deuce"
            return f"{self.POINTS_TO_SCORE[self.player1_score]}-All"
        
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self._get_end_game_score()
            
        return self._get_regular_score()
    
    def _get_end_game_score(self):
        point_difference = self.player1_score - self.player2_score
        
        if point_difference == 1:
            return "Advantage player1"
        if point_difference == -1:
            return "Advantage player2"
        if point_difference >= 2:
            return "Win for player1"
        return "Win for player2"
    
    def _get_regular_score(self):
        return f"{self.POINTS_TO_SCORE[self.player1_score]}-{self.POINTS_TO_SCORE[self.player2_score]}"
