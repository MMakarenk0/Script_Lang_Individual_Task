from Tower import *
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE | NOFRAME)
pygame.display.set_caption("Tower of Hanoi")

stepCounter = 0

font = pygame.font.Font(None, 36)

towers = []
for i in range(3):
    tower = Tower(i+1)
    towers.append(tower)

disks = []
for i in range(Disk.diskNumber):
    disk = Disk(towers[0], i)
    disks.append(disk)

for disk in disks:
    towers[0].addDisk(disk)

prevDiskNumber = Disk.diskNumber
sortedMoves = []
running = True
while running:
    screen.fill(BLACK)

    if prevDiskNumber != Disk.diskNumber:
        stepCounter, towers, disks, sortedMoves = Tower.reset(towers, disks)
        prevDiskNumber = Disk.diskNumber

    addList = []
    delList = []
    pygame.draw.rect(screen, (WHITE), (0, half_height, screen_width-2, 10), 2)
    if len(towers[2].availableDisks) == Disk.diskNumber: 
        screen.blit(font.render("Congratulations!", True, YELLOW), (half_width-100, half_height+100))

    if sortedMoves:
        Tower.moveDisks([sortedMoves[0][1], sortedMoves[0][2]], [sortedMoves[0][0]], towers, disks)
        sortedMoves.pop(0)
        stepCounter += 1
        pygame.time.delay(Disk.delay)
        for tower in towers:
            tower.simpleDraw(screen)
        
    else:
        for tower in towers:
                newAddList, newDelList = tower.drawTower(towers, screen, disks)
                if newAddList and newDelList:
                    addList.extend(newAddList)
                    delList.extend(newDelList)
        if addList and delList:
            Tower.moveDisks(addList, delList, towers, disks)
            stepCounter += 1
    
    
    screen.blit(font.render(f"Step: {stepCounter}", True, YELLOW), (half_width-25, screen_height-100))
    screen.blit(font.render("Press R to reset", True, YELLOW), (25, screen_height-100))
    screen.blit(font.render("Press F to auto-mode", True, YELLOW), (25, screen_height-200))
    Disk.drawDiskButtons(screen)
    screen.blit(font.render(f"Disk quantity: {Disk.diskNumber}", True, YELLOW), (screen_width-280, screen_height-100))
    Disk.drawDelayButtons(screen)
    screen.blit(font.render(f"Time delay: {Disk.delay/1000}", True, YELLOW), (screen_width-280, screen_height-200))


 
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                stepCounter, towers, disks, sortedMoves = Tower.reset(towers, disks)
            if event.key == pygame.K_f:
                stepCounter, towers, disks, sortedMoves = Tower.reset(towers, disks)
                n = Disk.diskNumber
                moves = towers[0].solve(n, towers[2], towers[1])
                sortedMoves = Tower.flatten_list(moves)
                sortedMoves = Tower.splitToGroups(sortedMoves, 3)
                stepCounter, towers, disks, _ = Tower.reset(towers, disks)
            if event.key == pygame.K_LSHIFT:
                Disk.shiftPressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                Disk.shiftPressed = False
            
    clock.tick(60)