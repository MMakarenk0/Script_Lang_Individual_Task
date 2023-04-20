import pygame

class Cell():
    def __init__(self, status=False, width=25, height=25, index=0):
        self.status = status
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.index = index
        self.row = index//(screen_width // (cell_width + 1))
        self.col = index - (index//(screen_width // (cell_width + 1)))*(screen_width // (cell_width + 1))
    
    def prepare(self, x, y):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.rect.topleft = (x, y)


        if self.status == True:
            if self.rect.collidepoint(mouse):
                pygame.draw.rect(screen, (255, 128, 128), (x, y, self.width, self.height))
                if click[0] == 1:
                    pygame.time.delay(100)
                    self.status = False
            else:
                pygame.draw.rect(screen, (255, 0, 0), (x, y, self.width, self.height))

        else:
            if self.rect.collidepoint(mouse):
                pygame.draw.rect(screen, (163, 163, 163), (x, y, self.width, self.height))
                if click[0] == 1:
                    pygame.time.delay(100)
                    self.status = True
            else:
                pygame.draw.rect(screen, (255, 255, 255), (x, y, self.width, self.height))


    def draw(self, x, y, cell_list):

        if self.status == True:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, self.width, self.height))
            activeNumber = 0
            for row in range(self.row-1, self.row+2):
                for col in range(self.col-1, self.col+2):
                    if row >= 0 and col >= 0 and row < len(cell_list) // (screen_width // (cell_width + 1)) and col < (screen_width // (cell_width + 1)):
                        if cell_list[row*(screen_width // (cell_width + 1)) + col].status == True:
                            activeNumber += 1
            if activeNumber < 3 or activeNumber > 4:
                markedCells.append(self)
        else:
            pygame.draw.rect(screen, (255, 255, 255), (x, y, self.width, self.height))
            activeNumber = 0
            for row in range(self.row-1, self.row+2):
                for col in range(self.col-1, self.col+2):
                    if row >= 0 and col >= 0 and row < len(cell_list) // (screen_width // (cell_width + 1)) and col < (screen_width // (cell_width + 1)):
                        if cell_list[row*(screen_width // (cell_width + 1)) + col].status == True:
                            activeNumber += 1
            if activeNumber == 3:
                markedCells.append(self)

            
    def cellInversion(self, markedCells):
        for cell in markedCells:
            cell.status = not(cell.status)
        markedCells.clear()

    def killAll(self, cell_list):
        for cell in cell_list:
            cell.status = False

    def saveAll(self, cell_list):
        for cell in cell_list:
            cell.status = True


    def getInfo():
        print("""
        Welcome to "Game of life"! 

        Rules of the game:

        Any live cell with fewer than two live neighbours dies, as if by underpopulation.

        Any live cell with two or three live neighbours lives on to the next generation.

        Any live cell with more than three live neighbours dies, as if by overpopulation.

        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        
        To start play activate some cells(click on them).

        'Space' - start/stop game.
        
        'C' - Clear whole screen.

        '+' - increase game speed.

        '-' - decrease game speed.
        
        Author: Maksym Makarenko.
        """)



clock = pygame.time.Clock()

pygame.init()

res = (798, 630)
screen_width = res[0]
screen_height = res[1]

cell_width = 20
cell_height = 20

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game of life")

Cell.getInfo()

bg = pygame.Surface((screen_width, screen_height))
bg.fill((122, 122, 122))

markedCells = []
cell_list = []
index = 0
delay = 300

for y in range(0, screen_height, cell_height+1):
    for x in range(0, screen_width, cell_width+1):
        cell = Cell(False, cell_width, cell_height, index)
        cell_list.append(cell)
        index += 1


working = True
while working:
    preparing = True
    while preparing:
        screen.blit(bg, (0, 0))

        
        for i, cell in enumerate(cell_list):
            x = (i % (screen_width // (cell_width + 1))) * (cell_width + 1)
            y = (i // (screen_width // (cell_width + 1))) * (cell_height + 1)
            cell.prepare(x, y)
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pygame.time.delay(150)
            preparing = False
        elif keys[pygame.K_c]:
            pygame.time.delay(150)
            cell.killAll(cell_list)
        elif keys[pygame.K_v]:
            pygame.time.delay(150)
            cell.saveAll(cell_list)


        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                working = False
                preparing = False
                pygame.quit()

        clock.tick(60)


    running = True
    while running:

        screen.blit(bg, (0, 0))

        
        for i, cell in enumerate(cell_list):
            x = (i % (screen_width // (cell_width + 1))) * (cell_width + 1)
            y = (i // (screen_width // (cell_width + 1))) * (cell_height + 1)
            cell.draw(x, y, cell_list)

        cell.cellInversion(markedCells)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pygame.time.delay(150)
            running = False
        elif keys[pygame.K_c]:
            pygame.time.delay(150)
            cell.killAll(cell_list)
        elif keys[pygame.K_v]:
            pygame.time.delay(150)
            cell.saveAll(cell_list)
        elif keys[pygame.K_EQUALS]:
            pygame.time.delay(150)
            delay -= 100
        elif keys[pygame.K_MINUS]:
            pygame.time.delay(150)
            delay += 100
        pygame.time.delay(delay)               
            
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        clock.tick(60)