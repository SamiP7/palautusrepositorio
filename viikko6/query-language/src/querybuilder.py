from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or, All

class QueryBuilder:
    def __init__(self, matcher = None):
        self.matcher = matcher or All()

    def build(self):
        return self.matcher

    def playsIn(self, team):
        
        
        return QueryBuilder(And(self.matcher, PlaysIn(team)))

    

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))

    def oneOf(self, query1, query2):
        return QueryBuilder(Or(query1, query2))