from matchers import And, Or, HasAtLeast, HasFewerThan, PlaysIn, All

class QueryBuilder:
    def __init__(self):
        self._matcher = All()
    
    def plays_in(self, team):
        self._matcher = And(self._matcher, PlaysIn(team))
        return self
    
    def has_at_least(self, value, attr):
        self._matcher = And(self._matcher, HasAtLeast(value, attr))
        return self
    
    def has_fewer_than(self, value, attr):
        self._matcher = And(self._matcher, HasFewerThan(value, attr))
        return self
    
    def build(self):
        return self._matcher
        
    def one_of(self, *matchers): #oletan että tehtävänannossa on virhe ja tämän pitäisi tehdä jotain eikä olla turha
        self._matcher = Or(*matchers)
        return self