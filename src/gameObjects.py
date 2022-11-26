import pygame
from core.gameObject import GameObject
"""@todo Cuando aumentas el tamaño las piezas no cambian la ubicación, mas bien se quedan asi siempre, una de la solucion que me imagino es hacer que cada pieza tenga su repectivas coordenadas y despues hacer que esas coordenadas determine el movimiento."""
BLACK=False;
WHITE=True;
image_piece={
    "pawn":[pygame.image.load('./pieces/PawnWhite.png'),pygame.image.load('./pieces/PawnBlack.png')],
    "knight":[pygame.image.load('./pieces/KnightWhite.png'),pygame.image.load('./pieces/KnightBlack.png')],
    "bishop":[pygame.image.load('./pieces/BishopWhite.png'),pygame.image.load('./pieces/BishopBlack.png')],
    "rook":[pygame.image.load('./pieces/RookWhite.png'),pygame.image.load('./pieces/RookBlack.png')],
    "queen":[pygame.image.load('./pieces/QueenWhite.png'),pygame.image.load('./pieces/QueenBlack.png')],
    "king":[pygame.image.load('./pieces/KingWhite.png'),pygame.image.load('./pieces/KingBlack.png')]
};
WIDTH_COLS=12.5;# Este es el largo de la columnas, se esta usando porcentaje para que sea dinamico el tamaño de las filas.
HEIGHT_COLS=12.5;# Este es el ancho de la columnas, tambien en porcentajes.
class Chessboard(GameObject):
    def __init__(self, game, *args, **kwargs):
        super(Chessboard, self).__init__(game, *args, **kwargs)
        """Aqui dibujaremos la tabla y crearemos las coordenadas.
        game -- La ventana como tal"""
        self.cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] #Columnas
        self.update_coors(game.size[0],game.size[1]);
    
    def update_coors(self,width:int,height:int):
        """Aqui creamos las coordenadas y ubicaciones de las piezas"""
        x, y, self.positions = 0, 0, {}
        self.width_cols=int((WIDTH_COLS*width)/100);#Calculamos el porcentaje y lo tansformamos a entero.
        self.height_cols=int((HEIGHT_COLS*height)/100);
        for x in range(len(self.cols)):
            for y in range(0,8):
                self.positions[self.cols[x]+str(y+1)] = (
                        (self.width_cols*x)+int(self.width_cols/2), # Calculamos la posicion x actual
                        (self.height_cols*y)+int(self.height_cols/2)); #Calculamos la posicion y actual
    
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
        """Aqui dibujamos el tablero."""
        c = 1 # 1=white, -1 black.
        for x in range(len(self.cols)):
            for y in range(0,8):
                pygame.draw.rect(self.game.screen,
                    (255, 206, 158) if c==1 else (209, 139, 71), #White or black colors
                    (x*self.width_cols, y*self.height_cols,self.width_cols,self.height_cols));#(81, 157, 255)
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
        self.value = team
        White=0 if team else 1; #Es para saber si 
        self.chessboard = chessboard
        print(self.chessboard)
        self.pieces = {
            'pawn1': Pawn(self.game, self, chessboard.positions),
            'pawn2': Pawn(self.game, self, chessboard.positions),
            'pawn3': Pawn(self.game, self, chessboard.positions),
            'pawn4': Pawn(self.game, self, chessboard.positions),
            'pawn5': Pawn(self.game, self, chessboard.positions),
            'pawn6': Pawn(self.game, self, chessboard.positions),
            'pawn7': Pawn(self.game, self, chessboard.positions),
            'pawn8': Pawn(self.game, self, chessboard.positions),
            'rook1': Piece(self.game, self, image_piece["rook"][White], chessboard.positions),
            'rook2': Piece(self.game, self, image_piece["rook"][White], chessboard.positions),
            'knight1': Piece(self.game, self, image_piece["knight"][White], chessboard.positions),
            'knight2': Piece(self.game, self, image_piece["knight"][White], chessboard.positions),
            'bishop1': Piece(self.game, self, image_piece["bishop"][White], chessboard.positions),
            'bishop2': Piece(self.game, self, image_piece["bishop"][White], chessboard.positions),
            'queen': Piece(self.game, self, image_piece["queen"][White], chessboard.positions),
            'king': Piece(self.game, self, image_piece["king"][White], chessboard.positions),
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
        self.enemyPieces = [ ]
        self.alliedPiece = [ ]

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
    def __init__(self, game, team, positions, *args, **kwargs):
        Piece.__init__(self,game,team,image_piece["pawn"][0 if team.value else 1], positions, *args, **kwargs);
        #Necesitamos que se mueva en el primer instante en dos o una casilla.
        """class Piece(GameObject):
            def __init__(self, game, team, image, positions, *args, **kwargs):"""

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
        print(movements)
        return movements

class Rook(Piece):
    def __init__(self):
        super().__init__(self);
        self.name="rook";

class Knight(Piece):
    def __init__(self):
        super(Piece,self).__init__(self);

class Bishop(Piece):
    def __init__(self):
        super(Piece,self).__init__(self);

class Queen(Piece):
    def __init__(self):
        super(Piece,self).__init__(self);

class King(Piece):
    def __init__(self):
        super(Piece,self).__init__(self);