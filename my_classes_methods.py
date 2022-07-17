class Gamer:
    active_gamers = 0
    @classmethod
    def get_amount(cls):
        return cls.active_gamers
    @classmethod
    def add_gamer_from_string(cls,str):
        nickname, age, level, points = \
            str.split(',')
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age=18, level=0, points=0):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers +=1;
    def is_adult(self):
        return self.age >= 18

class Admin(Gamer):
    def __init__(self, nickname, age=18, level=50, points=1000, experience = 10):
        Gamer.__init__(self, nickname, age, level, points)
        self.experience = experience

# gamer_1 = Gamer("Nick")
# print(Gamer.get_amount())
gamer = Gamer.add_gamer_from_string("Nick, 21, 7, 35")
print(gamer.age)