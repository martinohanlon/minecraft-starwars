import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as mcstuff
import math
from time import sleep
from random import randint

class DeathStar:
    def __init__(self, pos, radius):
        self.mc = minecraft.Minecraft.create()
        
        self.pos = pos
        self.radius = radius

        self._draw()

    def _draw(self):

        mcDraw = mcstuff.MinecraftDrawing(self.mc)
        
        #create hollow sphere for death star
        mcDraw.drawHollowSphere(self.pos.x, self.pos.y, self.pos.z, self.radius, block.WOOL.id, 7)

        #create a gun
        self.gunX, self.gunY, self.gunZ = self._findPointOnSphere(self.pos.x, self.pos.y, self.pos.z,
                                                                  45, 25, self.radius)
        self.mc.setBlock(self.gunX, self.gunY, self.gunZ, block.WOOL.id, 14)

        #gunX, gunY, gunZ = self._findPointOnSphere(self.pos.x, self.pos.y, self.pos.z,
        #                                           45, 25, self.radius)
        
        #rotate around point and draw a circle
        #for angle in range(0,360,15):
        #    circleX, circleY, circleZ = self._findPointOnSphere(gunX, gunY, gunZ, angle, 155, 5)
        #    mc.setBlock(circleX, circleY, circleZ, block.WOOL.id, 15)

        #angles = ((45,17),(45,33),(37,25),(53,25))
        #for angle in angles:
        #    x,y,z = self._findPointOnSphere(self.pos.x, self.pos.y, self.pos.z,
        #                                    angle[0], angle[1], self.radius)
        #    self.mc.setBlock(x,y,z,block.WOOL.id,15)
        
        #gunX2, gunY2, gunZ2 = self._findPointOnSphere(self.pos.x, self.pos.y, self.pos.z,
        #                                              45, 25, int(self.radius + (self.radius / 2) + 1))

        #draw a sphere of black wool, outside the death star to create the divit
        #mcDraw.drawSphere(gunX, gunY, gunZ, int(self.radius - (self.radius / 2.5)), block.AIR.id, 15)
        #mcDraw.drawSphere(gunX2, gunY2, gunZ2, int(self.radius - (self.radius / 2.5) + 1), block.AIR.id)

        #create some black blocks over the surface
        #for count in range(0,200):
        #    angle = randint(0,359)
        #    pitch = randint(-90,90)
        #    x, y, z = self._findPointOnSphere(self.pos.x, self.pos.y, self.pos.z,
        #                                      angle, pitch, self.radius - 1)
        #    self.mc.setBlock(x, y, z, block.WOOL.id, 15)


        #create horizontal circle all the way round        
        mcDraw.drawHorizontalCircle(self.pos.x, self.pos.y, self.pos.z,
                                    self.radius, block.AIR.id)
        mcDraw.drawHorizontalCircle(self.pos.x, self.pos.y, self.pos.z,
                                    self.radius - 1, block.WOOL.id, 15)

    def fire(self, x, y, z, delayStart, delayEnd):

        #draw a red line between the gun and the point
        sleep(delayStart)
        mcDraw = mcstuff.MinecraftDrawing(self.mc)
        mcDraw.drawLine(self.gunX, self.gunY, self.gunZ,
                        x, y, z,
                        block.WOOL.id, 14)
        sleep(delayEnd)

        #clear the line
        mcDraw.drawLine(self.gunX, self.gunY, self.gunZ,
                        x, y, z,
                        block.AIR.id)

    def destroy(self):
        mcDraw = mcstuff.MinecraftDrawing(self.mc)
        mcDraw.drawSphere(self.pos.x, self.pos.y, self.pos.z,
                          self.radius, block.LAVA_STATIONARY.id)
        sleep(3)
        self.clear()

    def clear(self):
        mcDraw = mcstuff.MinecraftDrawing(self.mc)
        mcDraw.drawSphere(self.pos.x, self.pos.y, self.pos.z, self.radius, block.AIR.id)

    def _findPointOnSphere(self, cx, cy, cz, horizontalAngle, verticalAngle, radius):
        x = cx + (radius * (math.cos(math.radians(verticalAngle)) * math.cos(math.radians(horizontalAngle))))
        y = cy + (radius * (math.sin(math.radians(verticalAngle))))
        z = cz + (radius * (math.cos(math.radians(verticalAngle)) * math.sin(math.radians(horizontalAngle))))
        return self._roundXYZ(x, y, z)

    def _roundXYZ(self,x,y,z):
        return int(round(x,0)), int(round(y,0)), int(round(z,0))

#tests
if __name__ == "__main__":

    print "running"
    mc = minecraft.Minecraft.create()
    
    playerPos = mc.player.getTilePos()
    playerPos.y += 35

    deathStar = DeathStar(playerPos, 20)

    sleep(10)

    playerPos = mc.player.getTilePos()

    deathStar.fire(playerPos.x, playerPos.y, playerPos.z, 1, 5) 

    deathStar.clear()
