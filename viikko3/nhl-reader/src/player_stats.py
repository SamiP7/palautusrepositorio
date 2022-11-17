from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        top_score = list(filter(lambda x: x.nationality == nationality, self._players))
        top_score.sort(key=lambda x: x.points, reverse=True)

        return top_score
