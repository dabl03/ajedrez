import pygame

from core.game import BaseScene
from src.gameObjects import Chessboard, Team

class MainScene(BaseScene):

    def start(self):
        self.gameObjects['Chessboard'] = Chessboard(self.game)
        self.gameObjects['teamWhite'] = Team(self.game, self.gameObjects['Chessboard'])
        self.gameObjects['teamBlack'] = Team(self.game, self.gameObjects['Chessboard'], False)

        self.gameObjects['teamWhite'].addChessboardPieces(self.gameObjects['teamBlack'])
        self.gameObjects['teamBlack'].addChessboardPieces(self.gameObjects['teamWhite'])
        self.chessboardPositions = self.getGameObject('Chessboard').positions
        self.lastPieceSelected = None
        self.pieceSelected = None
        self.movements = None
        self.turn = True

    def update(self, events, keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # pylint: disable=E1101
                mousePos = pygame.mouse.get_pos()
                clickEscaque = self.getGameObject('Chessboard').escaque(mousePos[0], mousePos[1])
                # print(self.movements)
                if self.lastPieceSelected and self.movements and len(self.movements) > 0 and clickEscaque in self.movements:
                    self.lastPieceSelected.move(clickEscaque)
                    enemyTeam = self.getGameObject('teamBlack') if self.turn else self.getGameObject('teamWhite')
                    self.turn = not self.turn
                    self.lastPieceSelected = None
                    self.pieceSelected = None
                    for enemyPiece in enemyTeam.pieces.values():
                        if enemyPiece.escaque == clickEscaque:
                            print("SHINEEEE!!!")
                            enemyPiece.kill()
                else:
                    for i in list(self.getGameObject('teamBlack').pieces.values()) + list(self.getGameObject('teamWhite').pieces.values()):
                        if clickEscaque is i.escaque:
                            self.movements = None
                            self.pieceSelected = i
                            if self.pieceSelected.team.value == self.turn:
                                self.lastPieceSelected = self.pieceSelected
                                self.movements = self.lastPieceSelected.possibleMovements()
                            else:
                                print('It is not the turn of this team.')
                print(self.turn)
