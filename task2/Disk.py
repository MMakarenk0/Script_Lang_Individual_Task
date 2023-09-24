import random
import pygame
from settings import *

prevClick = False

class Disk:
    diskNumber = 3
    delay = 500
    shiftPressed = False
    def __init__(self, tower, index):
        self.index = index
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.tower = tower
    
    def setTower(self, newTower):
        self.tower = newTower
    
    def getTower(self):
        return self.tower

    def getIndex(self):
        return self.index
    
    def drawDiskButtons(screen):
        global prevClick
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()  
        xm, ym = mouse 
        
        if xm > 1465 and xm < 1491 and ym > 750 and ym < 770:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 770), (1478, 750), (1491, 770)), 4)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 780), (1478, 800), (1491, 780)), 3)
            if click[0] == 1 and not prevClick:
                if Disk.diskNumber < 8:
                    Disk.diskNumber += 1
                    prevClick = True
            elif click[0] == 0:
                prevClick = False
        elif xm > 1465 and xm < 1491 and ym > 780 and ym < 800:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 770), (1478, 750), (1491, 770)), 3)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 780), (1478, 800), (1491, 780)), 4)
            if click[0] == 1 and not prevClick:
                if Disk.diskNumber > 3:
                    Disk.diskNumber -= 1
                    prevClick = True
            elif click[0] == 0:
                prevClick = False
        else:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 770), (1478, 750), (1491, 770)), 3)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 780), (1478, 800), (1491, 780)), 3)
    
    def drawDelayButtons(screen):
        global prevClick
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()  
        xm, ym = mouse 

        if xm > 1465 and xm < 1491 and ym > 650 and ym < 670:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 670), (1478, 650), (1491, 670)), 4)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 680), (1478, 700), (1491, 680)), 3)
        
            if click[0] == 1 and not prevClick and not Disk.shiftPressed:
                if Disk.delay < 2000:
                    Disk.delay += 100
                    prevClick = True
            elif click[0] == 1 and not prevClick and Disk.shiftPressed:
                if Disk.delay + 500 < 2000:
                    Disk.delay += 500
                    prevClick = True
                else:
                    Disk.delay = 2000
                    prevClick = True
            elif click[0] == 0:
                prevClick = False
        elif xm > 1465 and xm < 1491 and ym > 680 and ym < 700:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 670), (1478, 650), (1491, 670)), 3)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 680), (1478, 700), (1491, 680)), 4)
        
            if click[0] == 1 and not prevClick and not Disk.shiftPressed:
                if Disk.delay > 0:
                    Disk.delay -= 100
                    prevClick = True
            elif click[0] == 1 and not prevClick and Disk.shiftPressed:
                if Disk.delay - 500 > 0:
                    Disk.delay -= 500
                    prevClick = True
                else:
                    Disk.delay = 0
                    prevClick = True
            elif click[0] == 0:
                prevClick = False
        else:
            pygame.draw.lines(screen, YELLOW, True, ((1465, 670), (1478, 650), (1491, 670)), 3)
            pygame.draw.lines(screen, YELLOW, True, ((1465, 680), (1478, 700), (1491, 680)), 3)