from Disk import *

isHolding = False
holdingDiskIndex = 0

class Tower:
    def __init__(self, index):
        self.availableDisks = []
        self.index = index
    def getDiskList(self):
        return self.availableDisks
    def addDisk(self, disk):
        self.availableDisks.append(disk)
    def getTopDisk(self):
        return self.availableDisks[-1]

    def drawTower(self, towers, screen, disks):
        global isHolding
        global holdingDiskIndex
        addList = []
        delList = []
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()  
        xm, ym = mouse 
        
        forthPart = screen_width//4
        pygame.draw.rect(screen, (WHITE), (forthPart*self.index, half_height-202, 10, 200), 2)

        for i in range(len(self.availableDisks)):
            
            disk = self.availableDisks[i]
            
            diskSize = (50*(Disk.diskNumber - disk.index))/Disk.diskNumber/0.2
            collisionRect = pygame.Rect((((forthPart*self.index-diskSize//2)+4), (half_height-20-20*i), diskSize, 15))

            # When mouse on the top disk:
            if collisionRect.collidepoint(mouse) and disk == self.getTopDisk() and not isHolding:
                if click[0] == 1:
                    isHolding = True
                    if i == len(self.availableDisks)-1:
                        holdingDiskIndex = disk.index
                        if disk.index == holdingDiskIndex:
                            pygame.draw.rect(screen, disk.color, (xm, ym, diskSize, 15), 8)
                else:
                    isHolding = False
                    pygame.draw.rect(screen, disk.color, (((forthPart*self.index-diskSize//2)+4), (half_height-20-20*i), diskSize, 15), 8)

            # When holding:
            elif isHolding:
                if click[0] == 1:
                    isHolding = True
                    if i == len(self.availableDisks)-1 and disk.index == holdingDiskIndex:
                        pygame.draw.rect(screen, disk.color, (xm-diskSize//2, ym-7, diskSize, 15), 8)
                    else:
                        pygame.draw.rect(screen, disk.color, (((forthPart*self.index-diskSize//2)+4), (half_height-20-20*i), diskSize, 15), 4)
                else:
                    originTower = disks[holdingDiskIndex].getTower()
                    isHolding = False
                    if xm > (forthPart*(1)-112) and xm < (forthPart*(1)+112) and ym > half_height-200 and ym < half_height:
                        
                        if towers[0].getDiskList() and towers[0].getTopDisk().getIndex() < holdingDiskIndex:
                            
                            addList.append([0, holdingDiskIndex])
                            delList.append(originTower.index)
                            originTower.availableDisks[-1].tower = towers[0]

                        elif not towers[0].getDiskList():
                            addList.append([0, holdingDiskIndex])
                            delList.append(originTower.index)
                            originTower.availableDisks[-1].tower = towers[0]


                    elif xm > forthPart*(2)-112 and xm < forthPart*(2)+112 and ym > half_height-200 and ym < half_height:

                        if towers[1].getDiskList() and towers[1].getTopDisk().getIndex() < holdingDiskIndex:
                            
                            addList.append([1, holdingDiskIndex])
                            delList.append(originTower.index)
                            originTower.availableDisks[-1].tower = towers[1]
                        elif not towers[1].getDiskList():
                            addList.append([1, holdingDiskIndex])
                            delList.append(originTower.index)
                            originTower.availableDisks[-1].tower = towers[1]
                    elif xm > forthPart*(3)-112 and xm < forthPart*(3)+112 and ym > half_height-200 and ym < half_height:

                        if towers[2].getDiskList() and towers[2].getTopDisk().getIndex() < holdingDiskIndex:
                            
                            addList.append([2, holdingDiskIndex])
                            delList.append(originTower.index)
                            originTower.availableDisks[-1].tower = towers[2]
                        elif not towers[2].getDiskList():
                            addList.append([2, holdingDiskIndex])
                            delList.append(originTower.index)     
                            originTower.availableDisks[-1].tower = towers[2]           
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
            try:
                target.addDisk(disk)
                self.availableDisks.pop()
            except:
                pass
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

    def reset(towers, disks):
        sortedMoves = []
        for tower in towers:
            tower.availableDisks = []
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
        return 0, towers, disks, sortedMoves

    def simpleDraw(self, screen):
        forthPart = screen_width//4
        pygame.draw.rect(screen, (WHITE), (forthPart*self.index, half_height-202, 10, 200), 2)
        for i in range(len(self.availableDisks)):
            disk = self.availableDisks[i]
            diskSize = (50*(Disk.diskNumber - disk.index))/Disk.diskNumber/0.2
            pygame.draw.rect(screen, disk.color, (((forthPart*self.index-diskSize//2)+4), (half_height-20-20*i), diskSize, 15), 4)
