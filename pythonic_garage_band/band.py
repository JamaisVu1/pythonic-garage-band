class Band:
    count = 0
    instances = []
    
    def __init__(self, name, members):
        self.name = name
        Band.count += 1
        self.members = members
        Band.instances.append(self)
        
    def play_solos(self):
        return [member.play_solo() for member in self.members]
    
    @classmethod
    def to_list(cls):
        return cls.instances
        



class Musician:
    count = 0

    def __init__(self, name="unknown"):
        self.name = name
        Musician.count += 1



class Guitarist(Musician):
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

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
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

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
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
    
    def play_solo(self):
        return "rattle boom crash"