
from views.setting import Setting


class Match:
    def __init__(self, name, players_pair):
        self.player1 = players_pair[0]
        self.score_player1 = 0
        self.player2 = players_pair[1]
        self.score_player2 = 0
        self.winner = ""
        self.name = name

    def __repr__(self):
        return ([self.player1, self.score_player1],
                [self.player2, self.score_player2])


    def play_match(self):


        # Match joué, on rentre les scores
        print()
        winner = Setting().get_user_entry(
            msg_display=f"{self.player1.first_name} VS " +
                        f"{self.player2.first_name} \n"
                        f"Qui est le gagnant ?\n"
                        f"1 - {self.player1.first_name} \n"
                        f"2 - {self.player2.first_name} \n"
                        f"0 - Egalite\n",
            msg_error="Veuillez entrer 0, 1 ou 2.",
            value_type="selection",
            assertions=["0", "1", "2"]
        )

        if winner == "1":
            self.winner = self.player1.first_name
            self.score_player1 += 1
        elif winner == "2":
            self.winner = self.player2.first_name
            self.score_player2 += 1
        elif winner == "0":
            self.winner = "Egalite"
            self.score_player1 += 0.5
            self.score_player2 += 0.5

        self.player1.tournament_score += self.score_player1
        self.player2.tournament_score += self.score_player2

    def get_serialized_match(self):
        return {
            "player1": self.player1.get_serialized_player(save_turnament_score=True),
            "score_player1": self.score_player1,
            "player2": self.player2.get_serialized_player(save_turnament_score=True),
            "score_player2": self.score_player2,
            "winner": self.winner,
            "name": self.name
        }