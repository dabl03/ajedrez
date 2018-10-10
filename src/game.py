from core.game import BaseGame
from src.scenes import MainScene

class Game(BaseGame):

    def __init__(self, screenWidth=600, screenHeight=600, *args, **kwargs):
        super(Game, self).__init__(screenWidth, screenHeight, *args, **kwargs)
        self.scenes = [
            MainScene(self)
        ]
