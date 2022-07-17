
class Swimmable:
    def __init__(self, name=""):
        self.name = name
    def greeting(self):
        print(f"My name is {self.name} and I can swim")

class Walkable:
    def __init__(self, name=""):
        self.name = name
    def greeting(self):
        print(f"My name is {self.name} and I can walk")

class Flyable:
    def __init__(self, name=""):
        self.name = name
    def greeting(self):
        print(f"My name is {self.name} and I can fly")

class GameCharacter(Swimmable, Walkable, Flyable):
    def __init__(self, name=""):
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)
    def greeting(self):
        print(f"My name is {self.name}")
