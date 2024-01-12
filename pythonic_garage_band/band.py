class Band:
    count = 0
    
    def __init__(self, name, members):
        self.name = name
        Band.count += 1
        self.members = members



class Musician:
    count = 0

    def __init__(self, name="unknown"):
        self.name = name
        Musician.count += 1



class Guitarist:
    count = 0

    def __init__(self, name="unknown"):
        self.name = name
        Guitarist.count += 1

    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "guitar"


class Bassist:
    count = 0

    def __init__(self, name="unknown"):
        self.name = name
        Bassist.count += 1

    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

class Drummer:
    count = 0

    def __init__(self, name="unknown"):
        self.name = name
        Drummer.count += 1
        
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    def get_instrument(self):
        return "drums"