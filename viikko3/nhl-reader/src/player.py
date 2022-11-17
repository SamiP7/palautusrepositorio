class Player:
    def __init__(self, name, nationality, assists, goals, team):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team
    
    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals} {self.assists} = {self.points}"
