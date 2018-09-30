"""
CPSC 386 - Ping Pong Game
Create a Pong game for 2 players
Player 1 Movement Keys: Arrows Keys
Player 2 Movement Keys: W A S D
Name: DAI KIEU
"""
from math import sqrt


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.__x, self.__y, self.__z = x, y, z

    def __str__(self): return 'Point(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'

    def getx(self): return self.__x
    def gety(self): return self.__y
    def getz(self): return self.__z

    def setx(self, val): self.__x = val
    def sety(self, val): self.__y = val
    def setz(self, val): self.__z = val

    x = property(getx, gety)
    y = property(gety, sety)
    z = property(getz, setz)

    def distance(self, other):
        delx = self.x - other.x
        dely = self.y - other.y
        delz = self.z - other.z
        return sqrt(delx ** 2 + dely ** 2 + delz ** 2)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __add__(self, other):
        o = other
        return Vector(self.x + o.x, self.y + o.y, self.z + o.z)

    def __iadd__(self, other): return self + other

    def __isub__(self, other): return self - other
