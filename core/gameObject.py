class Transform:
    def __init__(self, x=0, y=0, *args, **kwargs):
        self.positionX = x
        self.positionY = y
    
    @property
    def x(self):
        return self.positionX
    @property
    def y(self):
        return self.positionY

    def translate(self, x, y):
        self.positionX += x
        self.positionY += y
    
    def setPosition(self, x, y):
        self.positionX = x
        self.positionY = y
    
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class GameObject:
    def __init__(self, game, *args, **kwargs):
        self.game = game
        self.transform = Transform()
    def draw(self): pass
    def start(self): pass
    
    def __str__(self):
        return '<{}({}, {})>'.format(str(self.__class__)[8:-2], self.transform.x, self.transform.y)
