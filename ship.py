from random import randint

class Ship(object):
    'Ship object'

    def __init__(self, name, hitLimit):
        self.name = name
        self.hitLimit = hitLimit 
        self.hitCount = 0
        self.coords = self.assignCoords(hitLimit)
        self.destroyed = False

    def assignCoords(self, hitLimit):
        coords = []
        if randint(0,1) > 0: #aligns vertical
            col = chr(65 + randint(0,9))
            startrow = randint(0, 9 - hitLimit)
            for i in range(0, hitLimit):
                coords.append(col + str(i + startrow))
        else: #aligns horizontal
            row = randint(0,9)
            startcol = randint(0, 9 - hitLimit)
            for i in range(0, hitLimit):
                coords.append(chr(startcol + 65 + i) + str(row))
        return coords

    def hit(self):
        if self.hitCount + 1 >= self.hitLimit:
            self.destroyed = True
        self.hitCount = self.hitCount + 1

    def checkCoords(self, coord):
        if coord in self.coords: #if coordinate is in ship, return true
            return True
        else:
            return False #else return false

    def __str__(self):
        return str(self.name) + "\n" + "Hit Limit: " +\
        str(self.hitLimit) + "\n" + "Coordinates: " + \
        str(self.coords)

class CompShip(Ship):
    'Ship controlled by computer'

    def __init__(self, name, hitLimit):
        super(CompShip, self).__init__(name, hitLimit)
        self.name = name
        self.hitLimit = hitLimit 
        self.hitCount = 0
        self.coords = self.assignCoords(hitLimit)
        self.destroyed = False

    def assignCoords(self, hitLimit):
        coords = []
        if randint(0,1) > 0: #aligns vertical
            col = chr(65 + randint(0,9))
            startrow = randint(0, 9 - hitLimit)
            for i in range(0, hitLimit):
                coords.append(col + str(i + startrow))
        else: #aligns horizontal
            row = randint(0,9)
            startcol = randint(0, 9 - hitLimit)
            for i in range(0, hitLimit):
                coords.append(chr(startcol + 65 + i) + str(row))
        return coords
        
    def __str__(self):
        return str(self.name) + "\n" + "Hit Limit: " +\
        str(self.hitLimit) + "\n" + "Coordinates: " + \
        str(self.coords)

class HumanShip(Ship):
    'Ship controlled by human'

    def assignCoords(self, hitLimit):
        coords = []
        if randint(0,1) > 0: #aligns vertical
            col = chr(65 + randint(0,9))
            startrow = randint(0, 9 - hitLimit)
            for i in range(0, hitLimit):
                coords.append(col + str(i + startrow))
        else: #aligns horizontal
            row = randint(0,9)
            startcol = randint(0, 9 - hitLimit)
            for i in range(0, hitLimit):
                coords.append(chr(startcol + 65 + i) + str(row))
        return coords

    def __str__(self):
        return str(self.name) + "\n" + "Hit Limit: " +\
        str(self.hitLimit) + "\n" + "Coordinates: " + \
        str(self.coords)