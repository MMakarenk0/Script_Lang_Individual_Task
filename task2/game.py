import pygame
from settings import *
import random
from pygame.locals import *


class Disk:
    diskNumber = 3
    delay = 500
    shiftPressed = False
    prev_click = False
    def __init__(self, tower, index):
        self.index = index
        self.color = (random.randint(25, 255), random.randint(25, 255), random.randint(25, 255))
        self.tower = tower
    
    def setTower(self, newTower):
        self.tower = newTower
    
    def getTower(self):
        return self.tower

    def getIndex(self):
        return self.index
    
    def drawDiskButtons(screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()      
        xm, ym = mouse 
        
        if xm > 1465 and xm < 1491 and ym > 750 and ym < 770:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 770), (1478, 750), (1491, 770)), 4)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 780), (1478, 800), (1491, 780)), 3)
            if click[0] == 1 and not Disk.prev_click and not Disk.shiftPressed:
                if Disk.diskNumber < 20:
                    Disk.diskNumber += 1
                    Disk.prev_click = True
            elif click[0] == 1 and not Disk.prev_click and Disk.shiftPressed:
                if Disk.diskNumber + 5 < 20 :
                    Disk.diskNumber += 5
                    Disk.prev_click = True
                else:
                    Disk.diskNumber = 20
                    Disk.prev_click = True
            elif click[0] == 0:
                Disk.prev_click = False
        elif xm > 1465 and xm < 1491 and ym > 780 and ym < 800:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 770), (1478, 750), (1491, 770)), 3)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 780), (1478, 800), (1491, 780)), 4)
            if click[0] == 1 and not Disk.prev_click and not Disk.shiftPressed:
                if Disk.diskNumber > 3:
                    Disk.diskNumber -= 1
                    Disk.prev_click = True
            elif click[0] == 1 and not Disk.prev_click and Disk.shiftPressed:
                if Disk.diskNumber - 5 > 3 :
                    Disk.diskNumber -= 5
                    Disk.prev_click = True
                else:
                    Disk.diskNumber = 3
                    Disk.prev_click = True
            elif click[0] == 0:
                Disk.prev_click = False
        else:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 770), (1478, 750), (1491, 770)), 3)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 780), (1478, 800), (1491, 780)), 3)
    
    def drawDelayButtons(screen):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()  
        xm, ym = mouse 

        if xm > 1465 and xm < 1491 and ym > 650 and ym < 670:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 670), (1478, 650), (1491, 670)), 4)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 680), (1478, 700), (1491, 680)), 3)
        
            if click[0] == 1 and not Disk.prev_click and not Disk.shiftPressed:
                if Disk.delay < 2000:
                    Disk.delay += 100
                    Disk.prev_click = True
            elif click[0] == 1 and not Disk.prev_click and Disk.shiftPressed:
                if Disk.delay + 500 < 2000:
                    Disk.delay += 500
                    Disk.prev_click = True
                else:
                    Disk.delay = 2000
                    Disk.prev_click = True
            elif click[0] == 0:
                Disk.prev_click = False
        elif xm > 1465 and xm < 1491 and ym > 680 and ym < 700:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 670), (1478, 650), (1491, 670)), 3)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 680), (1478, 700), (1491, 680)), 4)
        
            if click[0] == 1 and not Disk.prev_click and not Disk.shiftPressed:
                if Disk.delay > 0:
                    Disk.delay -= 100
                    Disk.prev_click = True
            elif click[0] == 1 and not Disk.prev_click and Disk.shiftPressed:
                if Disk.delay - 500 > 0:
                    Disk.delay -= 500
                    Disk.prev_click = True
                else:
                    Disk.delay = 0
                    Disk.prev_click = True
            elif click[0] == 0:
                Disk.prev_click = False
        else:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 670), (1478, 650), (1491, 670)), 3)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 680), (1478, 700), (1491, 680)), 3)

    

class Tower:
    def __init__(self, index):
        self.availableDisks = []
        self.index = index
        self.isHolding = False
        self.holding_disk_index = 0
    def getDiskList(self):
        return self.availableDisks
    def addDisk(self, disk):
        self.availableDisks.append(disk)
    def getTopDisk(self):
        return self.availableDisks[-1]

    def drawTower(self, towers, screen, disks):
        addList = []
        delList = []
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()  
        xm, ym = mouse 
        
        forthPart = screen_width//4
        pygame.draw.rect(screen, (WHITE), (forthPart*self.index, half_height-21*Disk.diskNumber, 10, 21*Disk.diskNumber), 2)

        for i in range(len(self.availableDisks)):
            
            disk = self.availableDisks[i]
            
            diskSize = (50*(Disk.diskNumber - disk.index))/Disk.diskNumber/0.2
            collisionRect = pygame.Rect((((forthPart*self.index-diskSize//2)+4), (half_height-20-20*i), diskSize, 15))

            # When mouse on the top disk:
            if collisionRect.collidepoint(mouse) and disk == self.getTopDisk() and not self.isHolding:
                if click[0] == 1:
                    self.isHolding = True
                    if i == len(self.availableDisks)-1:
                        self.holding_disk_index = disk.index
                        if disk.index == self.holding_disk_index:
                            pygame.draw.rect(screen, disk.color, (xm-diskSize//2, ym-7, diskSize, 15), 8)
                else:
                    self.isHolding = False
                    pygame.draw.rect(screen, disk.color, (((forthPart*self.index-diskSize//2)+4), (half_height-20-20*i), diskSize, 15), 8)

            # When holding:
            elif self.isHolding:
                if click[0] == 1:
                    self.isHolding = True
                    if i == len(self.availableDisks)-1 and disk.index == self.holding_disk_index:
                        pygame.draw.rect(screen, disk.color, (xm-diskSize//2, ym-7, diskSize, 15), 8)
                    else:
                        pygame.draw.rect(screen, disk.color, (((forthPart*self.index-diskSize//2)+4), (half_height-20-20*i), diskSize, 15), 4)
                else:
                    originTower = disks[self.holding_disk_index].getTower()
                    self.isHolding = False

                    # Checking collisions with all towers and saving all moves.
                    for tower_index, tower in enumerate(towers):
                        if xm > (forthPart*(tower_index+1)-112) and xm < (forthPart*(tower_index+1)+112) and ym > half_height-200 and ym < half_height:
                        
                            if tower.getDiskList() and tower.getTopDisk().getIndex() < self.holding_disk_index:
                                
                                addList.append([tower_index+1, self.holding_disk_index])
                                delList.append(originTower.index)
                                originTower.availableDisks[-1].tower = tower

                            elif not tower.getDiskList():
                                addList.append([tower_index+1, self.holding_disk_index])
                                delList.append(originTower.index)
                                originTower.availableDisks[-1].tower = tower      
            else:
                pygame.draw.rect(screen, disk.color, (((forthPart*self.index-diskSize//2)+4), (half_height-20-20*i), diskSize, 15), 4)
        if addList and delList:
            return addList, delList 
        else:
            return None, None
    
    def moveDisks(addList, delList, towers, disks):

        originTower = towers[delList[0]-1]
        try:
            targetTowerIndex, diskIndex = addList
        except ValueError:
            targetTowerIndex, diskIndex = addList[0]

        towers[targetTowerIndex-1].addDisk(disks[diskIndex])

        originTower.availableDisks.pop()
    
    def solve(self, n, target, auxiliary):
        moves = []
        if n == 1:
            disk = self.getTopDisk()
            
            target.addDisk(disk)
            self.availableDisks.pop()
            
            return [self.index, target.index, disk.index]
        else:
            moves.append(self.solve(n - 1, auxiliary, target))

            moves.append(self.solve(1, target, auxiliary))

            moves.append(auxiliary.solve(n - 1, target, self))

            return moves

    def flatten_list(nested_list):
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(Tower.flatten_list(item))
            else:
                flat_list.append(item)
        return flat_list

    def splitToGroups(lst, group_size):
        return [lst[i:i+group_size] for i in range(0, len(lst), group_size)]

    def simpleDraw(self, screen):
        forthPart = screen_width//4
        pygame.draw.rect(screen, (WHITE), (forthPart*self.index, half_height-21*Disk.diskNumber, 10, 21*Disk.diskNumber), 2)
        for i in range(len(self.availableDisks)):
            disk = self.availableDisks[i]
            diskSize = (50*(Disk.diskNumber - disk.index))/Disk.diskNumber/0.2
            pygame.draw.rect(screen, disk.color, (((forthPart*self.index-diskSize//2)+4), (half_height-20-20*i), diskSize, 15), 4)

class Game:
    def __init__(self):
        self.towers = []
        self.disks = []
        self.sorted_moves = []
        self.step_counter = 0
        self.canvas = Canvas()
    
    def reset_objs(self):
        self.step_counter = 0
        sorted_moves = []
        self.towers = []
        for i in range(3):
            tower = Tower(i+1)
            self.towers.append(tower)

        self.disks = []
        for i in range(Disk.diskNumber):
            disk = Disk(self.towers[0], i)
            self.disks.append(disk)

        for disk in self.disks:
            self.towers[0].addDisk(disk)

        return sorted_moves

    def run(self):
        # Method to start main loop

        pygame.init()

        clock = pygame.time.Clock()

        self.sorted_moves = self.reset_objs()

        prevDiskNumber = Disk.diskNumber
        running = True
        while running:
            
            if prevDiskNumber != Disk.diskNumber:
                self.sorted_moves = self.reset_objs()
                prevDiskNumber = Disk.diskNumber

            addList = []
            delList = []
            
            self.canvas.draw_background()

            # Win condition
            if len(self.towers[2].availableDisks) == Disk.diskNumber: 
                self.canvas.draw_text("Congratulations!", 36, half_width-100, half_height+100, YELLOW)

            # Drawing and moving disks
            if self.sorted_moves:
                Tower.moveDisks([self.sorted_moves[0][1], self.sorted_moves[0][2]], [self.sorted_moves[0][0]], self.towers, self.disks)
                self.sorted_moves.pop(0)
                self.step_counter += 1
                pygame.time.delay(Disk.delay)
                for tower in self.towers:
                    tower.simpleDraw(self.canvas.get_canvas())
            else:
                for tower in self.towers:
                        newAddList, newDelList = tower.drawTower(self.towers, self.canvas.get_canvas(), self.disks)
                        if newAddList and newDelList:
                            addList.extend(newAddList)
                            delList.extend(newDelList)
                if addList and delList:
                    Tower.moveDisks(addList, delList, self.towers, self.disks)
                    self.step_counter += 1
            
            


            # Drawing other stuff
            self.canvas.draw_text(f"Step: {self.step_counter}", 36, half_width-25, screen_height-100, YELLOW)
            self.canvas.draw_text("Press R to reset", 36, 25, screen_height-100, YELLOW)
            self.canvas.draw_text("Press F to activate algorithm", 36, 25, screen_height-200, YELLOW)
            self.canvas.draw_text(f"steps expected: {2**(Disk.diskNumber)-1}", 25, 25, screen_height-175, YELLOW)
            Disk.drawDiskButtons(self.canvas.get_canvas())
            self.canvas.draw_text(f"Disk quantity: {Disk.diskNumber}", 36, screen_width-280, screen_height-100, YELLOW)
            Disk.drawDelayButtons(self.canvas.get_canvas())
            self.canvas.showfps(clock, 25, screen_width-100, screen_height-30)
            self.canvas.draw_text(f"Time delay: {Disk.delay/1000}", 36, screen_width-280, screen_height-200, YELLOW)
            
        
            self.canvas.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.sorted_moves = self.reset_objs()
                    if event.key == pygame.K_f:
                        self.sorted_moves = self.reset_objs()
                        n = Disk.diskNumber
                        moves = self.towers[0].solve(n, self.towers[2], self.towers[1])
                        self.sorted_moves = Tower.flatten_list(moves)
                        self.sorted_moves = Tower.splitToGroups(self.sorted_moves, 3)
                        self.reset_objs()
                    if event.key == pygame.K_LSHIFT:
                        Disk.shiftPressed = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LSHIFT:
                        Disk.shiftPressed = False
                    


            clock.tick(FPS)

class Canvas:
    
    def __init__(self):
        self.width = screen_width
        self.height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE | NOFRAME)
        pygame.display.set_caption("Tower of Hanoi")

    @staticmethod
    def update():
        pygame.display.update()

    def draw_text(self, text, size, x, y, color):
        pygame.font.init()
        font = pygame.font.Font(None, size)
        render = font.render(text, 1, color)

        self.screen.blit(render, (x,y))
    
    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen, (WHITE), (0, half_height, screen_width-2, 10), 2)

    def showfps(self, clock, size, x, y):
        fps = int(clock.get_fps())
        if fps > 50: color = GREEN
        elif fps > 30: color = YELLOW
        else: color = RED
        self.draw_text(f"FPS: {fps}", size, x, y, color)
