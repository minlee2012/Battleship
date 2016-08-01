from ship import *

class Ships(object):
    'Collection of ship objects'

    def __init__(self):
        self.ShipList = []
        ACCarrier = Ship("Aircraft Carrier", 5)
        self.ShipList.append(ACCarrier)

        Battleship = Ship("Battleship", 4)
        while self.check(Battleship):
            Battleship = Ship("Battleship", 4)
        self.ShipList.append(Battleship)

        Submarine = Ship("Submarine", 3)
        while self.check(Submarine):
            Submarine = Ship("Submarine", 3)
        self.ShipList.append(Submarine)

        Destroyer = Ship("Destroyer", 3)
        while self.check(Destroyer):
            Destroyer = Ship("Destroyer", 3)
        self.ShipList.append(Destroyer)

        Patrol = Ship("Patrol Ship", 2) 
        while self.check(Patrol):
            Patrol = Ship("Patrol Ship", 2) 
        self.ShipList.append(Patrol)

    def check(self, checkingShip):
        for ship in self.ShipList:
            for coord in checkingShip.coords:
                if ship.checkCoords(coord): #if coordinate matches a ship coordinate
                    return True
                else:
                    pass
        return False

    def checkHit(self, coord):
        for ship in self.ShipList:
            if ship.checkCoords(coord): #if coordinate matches a ship coordinate
                return True
            else:
                pass
        return False

    def destroyedCheck(self):
        count = 0
        for ship in self.ShipList:
            if ship.destroyed:
                count = count + 1
        if count == len(self.ShipList):
            return True
        return False

    def returnHit(self, coord):
        for ship in self.ShipList:
            if ship.checkCoords(coord):
                return ship
        return None

    def __str__(self):
        return "".join("\n".join(str(self.ShipList[num]) for num in range(0, len(self.ShipList))))