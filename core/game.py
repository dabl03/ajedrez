import pygame
from core.errors import LoadSceneError

class BaseGame:
    pause = False
    frameRate = 60
    screen = None
    font = None

    def __init__(self, width, height, *args, **kwargs):
        pygame.init() #pylint: disable=E1101
        pygame.display.set_caption('Snake')
        pygame.font.init()
        self.size = self.width, self.height = width, height
        self.screen = pygame.display.set_mode(self.size)
        self.scenes = []
        self.scene = None
        self.clock = pygame.time.Clock()
        self.quitStatus = False

    def loadScene(self, scene=0):
        if len(self.scenes) >= 0 and scene < len(self.scenes) and isinstance(self.scenes[scene], BaseScene):
            self.scene = self.scenes[scene]
            self.scene.start()
            for value in self.scene.gameObjects.values():
                value.start()
        else:
            raise LoadSceneError("Error al cargar la escena")

    def run(self):
        self.loadScene()
        if isinstance(self.scene, BaseScene):
            while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT: self.quitGame() #pylint: disable=E1101
                if self.quitStatus:
                    break
                self.scene.update(events, pygame.key.get_pressed())
                self.scene.draw()
                pygame.display.update()
                self.clock.tick(self.frameRate)

    def quitGame(self):
        pygame.quit() #pylint: disable=E1101
        self.quitStatus = True

class BaseScene:
    def __init__(self, game, *args, **kwargs):
        self.gameObjects = {}
        self.game = game
        self.screen = game.screen
    
    def start(self): pass
    def update(self, events, keys): pass
    def draw(self):
        for key, value in self.gameObjects.items():
            value.draw()
    
    def getGameObject(self, name):
        if (name in self.gameObjects): return self.gameObjects[name]
        print('GameObject not found')
        return None