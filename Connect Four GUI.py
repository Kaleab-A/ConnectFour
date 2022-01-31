import pygame

class ConnectFour:
    def __init__(self, cell_size=(10, 10), board_size=(6, 7), dot_factor = 0.65, ontop = 5):
        self.cell_size = cell_size
        self.size_x = self.cell_size[0] * board_size[1]
        self.size_y = self.cell_size[1] * board_size[0]
        self.quit = False
        self.board_size = board_size
        self.dot_factor = dot_factor
        self.color = {"red" : (255, 0, 0), "blue" : (0, 0, 255), "green" : (0, 255, 0), "white" : (255, 255, 255), "black": (0, 0, 0)}
        self.board = [[0 for i in range(self.board_size[1])] for j in range(self.board_size[0])]
        self.color_board = [["blue" for i in range(self.board_size[1])] for j in range(self.board_size[0])]
        
        self.game_color = [(255, 0, 0), (0, 0, 255)]
        self.turn = 0

        pygame.init()

        self.screen = pygame.display.set_mode((self.size_x, self.size_y))

        self.update_screen()

    def update_screen(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.make_move("red")
                    self.draw_board()
            self.init_display()
            pygame.display.update()

            winner = self.isWinner()
            if winner != None:
                self.quit = True
                if winner == 1: print("Player 1 Wins")
                elif winner == 2: print("Player 2 Wins")


    def init_display(self):
        for i in range(1, self.board_size[1]):
            pygame.draw.line(self.screen, self.color["red"], (i*(self.size_x/self.board_size[1]), 0), (i*(self.size_x/self.board_size[1]), self.size_y))

        for i in range(1, self.board_size[0]):
            pygame.draw.line(self.screen, self.color["red"], (0, i*(self.size_y/self.board_size[0])), (self.size_x, i*(self.size_y/self.board_size[0])))

        
    def make_move(self, color):
        pos =  pygame.mouse.get_pos()
        pos_x, pos_y = [pos[1] // self.cell_size[1], pos[0] // self.cell_size[0]]
        for i in range(len(self.board)-1, -1, -1):
            if self.board[i][pos_y] == 0:
                pos_x = i
                break
        if self.board[pos_x][pos_y] == 0:
            self.board[pos_x][pos_y] = self.turn + 1
            self.color_board[pos_x][pos_y] = self.game_color[self.turn]
            self.turn = 1 - self.turn
        
        # for i in self.board:
            # print(i)

    def isWinner(self):
        row = len(self.board)
        col = len(self.board[0])

        for i in range(row):
            for j in range(col):
                if j + 3 < col and (self.board[i][j] != 0 and (self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3])):
                    return self.board[i][j]
                elif i + 3 < row and self.board[i][j] != 0 and (self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]):
                    return self.board[i][j]
                elif i + 3 < row and j + 3 < col and self.board[i][j] != 0 and (self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]):
                    return self.board[i][j]
                elif i + 3 < row and j - 3 >= 0 and self.board[i][j] != 0 and (self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]):
                    return self.board[i][j]
        return None

    def draw_board(self):
        for i in range(self.board_size[0]): 
            for j in range(self.board_size[1]):
                if self.board[i][j] != 0:
                    for k in range(self.board[i][j]):
                        draw_pos = (self.cell_size[1] * j + (self.cell_size[1] / 2),
                                    self.cell_size[0] * i + (self.cell_size[0] / 2))
                        
                        pygame.draw.circle(self.screen, self.color_board[i][j], draw_pos, (self.cell_size[0] / 2) * self.dot_factor)


game = ConnectFour((45, 45))