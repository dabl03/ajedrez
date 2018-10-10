import pygame
from core.gameObject import GameObject

class Chessboard(GameObject):
    def __init__(self, game, *args, **kwargs):
        super(Chessboard, self).__init__(game, *args, **kwargs)
        self.cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        n, m, positions = 0, 8, {}
        for i in range(0, self.game.size[0], 50):
            for j in range(0, self.game.size[1], 50):
                center = i+25, j+25
                positions[self.cols[n]+str(m)] = center
                m-=1
            n+=1
            m = 8
        self.positions = positions

    def letterOffset(self, letter, offset):
        try:
            i = self.cols.index(letter) + offset
            if i >= 0:
                return self.cols[i]
        except: pass
    
    def getRowOrCol(self, value):
        row = []
        for k in self.positions:
            if str(value).upper() in k:
                row.append((k, self.positions[k]))
        return row

    def draw(self):
        c = 1
        for i in range(0, self.game.size[0], 50):
            for j in range(0, self.game.size[1], 50):
                if c == 1: pygame.draw.rect(self.game.screen, (255, 206, 158), (i, j,50,50)) #(204, 204, 255)
                else: pygame.draw.rect(self.game.screen, (209, 139, 71), (i, j,50,50)) #(81, 157, 255)
                c *= -1
            c *= -1

    def escaque(self, x, y):
        for k, v in self.positions.items():
            if x in range(v[0]-25,v[0]+25) and y in range(v[1]-25,v[1]+25):
                return k

class Team(GameObject):
    def __init__(self, game, chessboard, team=True, *args, **kwargs):
        super().__init__(game, *args, **kwargs)
        self.name = 'White' if team else 'Black'
        self.value = True if team else False
        pawnImage = pygame.image.load('./pieces/PawnWhite.png') if team else pygame.image.load('./pieces/PawnBlack.png')
        knightImage = pygame.image.load('./pieces/KnightWhite.png') if team else pygame.image.load('./pieces/KnightBlack.png')
        bishopImage = pygame.image.load('./pieces/BishopWhite.png') if team else pygame.image.load('./pieces/BishopBlack.png')
        rookImage = pygame.image.load('./pieces/RookWhite.png') if team else pygame.image.load('./pieces/RookBlack.png')
        queenImage = pygame.image.load('./pieces/QueenWhite.png') if team else pygame.image.load('./pieces/QueenBlack.png')
        kingImage = pygame.image.load('./pieces/KingWhite.png') if team else pygame.image.load('./pieces/KingBlack.png')
        self.chessboard = chessboard
        self.pieces = {
            'pawn1': Pawn(self.game, self, pawnImage, chessboard.positions),
            'pawn2': Pawn(self.game, self, pawnImage, chessboard.positions),
            'pawn3': Pawn(self.game, self, pawnImage, chessboard.positions),
            'pawn4': Pawn(self.game, self, pawnImage, chessboard.positions),
            'pawn5': Pawn(self.game, self, pawnImage, chessboard.positions),
            'pawn6': Pawn(self.game, self, pawnImage, chessboard.positions),
            'pawn7': Pawn(self.game, self, pawnImage, chessboard.positions),
            'pawn8': Pawn(self.game, self, pawnImage, chessboard.positions),
            'rook1': Piece(self.game, self, rookImage, chessboard.positions),
            'rook2': Piece(self.game, self, rookImage, chessboard.positions),
            'knight1': Piece(self.game, self, knightImage, chessboard.positions),
            'knight2': Piece(self.game, self, knightImage, chessboard.positions),
            'bishop1': Piece(self.game, self, bishopImage, chessboard.positions),
            'bishop2': Piece(self.game, self, bishopImage, chessboard.positions),
            'queen': Piece(self.game, self, queenImage, chessboard.positions),
            'king': Piece(self.game, self, kingImage, chessboard.positions),
        }
        self.mount()
    
    def mount(self):
        row = self.chessboard.getRowOrCol(2 if self.value else 7)
        pawn = 1
        for i in row:
            self.pieces['pawn'+str(pawn)].transform.setPosition(i[1][0], i[1][1])
            self.pieces['pawn'+str(pawn)].move(i[0])
            pawn+=1
        row = self.chessboard.getRowOrCol(1 if self.value else 8)
        rook = 1
        knight = 1
        bishop = 1
        for i in row:
            if i[0][0] == 'A' or i[0][0] == 'H':
                self.pieces['rook'+str(rook)].move(i[0])
                rook+=1
            elif i[0][0] == 'B' or i[0][0] == 'G':
                self.pieces['knight'+str(knight)].move(i[0])
                knight+=1
            elif i[0][0] == 'C' or i[0][0] == 'F':
                self.pieces['bishop'+str(bishop)].move(i[0])
                bishop+=1
            elif i[0][0] == 'D':
                self.pieces['queen'].move(i[0])
            else:
                self.pieces['king'].move(i[0])

    def addChessboardPieces(self, enemyTeam):
        for piece in self.pieces.values():
            for alliedPiece in self.pieces.values():
                if piece != alliedPiece:
                    piece.addAlliedPiece(alliedPiece)
        self.enemyTeam = enemyTeam
        for piece in self.pieces.values():
            for enemyPiece in enemyTeam.pieces.values():
                piece.addEnemyPiece(enemyPiece)

    def draw(self):
        for piece in self.pieces.values():
            piece.draw()
    
    def getPieceIn(self, pos):
        for piece in self.pieces.values():
            if piece.escaque is pos: return piece

class Piece(GameObject):
    def __init__(self, game, team, image, positions, *args, **kwargs):
        super(Piece, self).__init__(game, *args, **kwargs)
        image = pygame.transform.smoothscale(image, (30, 30))
        self.live = True
        self.image = image
        self.positions = positions
        self.team = team
        self.escaque = None
        self.enemyPieces = []
        self.alliedPiece = []

    def draw(self):
        if self.escaque in self.positions and self.live:
            self.game.screen.blit(self.image, (self.transform.x-15, self.transform.y-15))

    def addEnemyPiece(self, piece):
        self.enemyPieces.append(piece)
    
    def addAlliedPiece(self, piece):
        self.alliedPiece.append(piece)
    
    def possibleMovements(self): return []

    def move(self, to):
        if to in self.positions:
            self.escaque = to
            self.transform.setPosition(self.positions[to][0], self.positions[to][1])
    
    def kill(self):
        self.live = False
        self.escaque = 'I9'
        self.transform.setPosition(-500, -500)

class Pawn(Piece):
    def possibleMovements(self):
        i = 1 if self.team.value else -1
        movements = []
        leftFrontPosition = self.team.chessboard.letterOffset(self.escaque[0], -1)
        frontPosition = [self.escaque[0] + str(int(self.escaque[1])+i), True]
        rightFrontPosition = self.team.chessboard.letterOffset(self.escaque[0], 1)
        positions = []
        if leftFrontPosition: positions.append([leftFrontPosition + str(int(self.escaque[1])+i), False]),
        else: positions.append(None)
        positions.append(frontPosition)
        if rightFrontPosition: positions.append([rightFrontPosition + str(int(self.escaque[1])+i), False])
        else: positions.append(None)

        for position in positions:
            if position:
                for piece in self.enemyPieces + self.alliedPiece:
                    if piece.live:
                        if piece.escaque == frontPosition[0] == position[0]:
                            position[1] = False
                        if piece.team.value != self.team.value and positions[0] and position[0] == piece.escaque == positions[0][0]:
                            positions[0][1] = True
                        if piece.team.value != self.team.value and positions[2] and position[0] == piece.escaque == positions[2][0]:
                            positions[2][1] = True
        for position in positions:
            if position and position[1]:
                movements.append(position[0])
        return movements
