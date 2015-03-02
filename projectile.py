from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi.minecraftstuff import MinecraftShape, MinecraftDrawing
from mcpi.minecraftstuff import ShapeBlock
from mcpi import block
from time import sleep
from threading import Thread

class Projectile:
    def __init__(self, projectileBlocks):

        self.mc = Minecraft.create()
        self.projectileBlocks = projectileBlocks

    def fire(self,x1,y1,z1,x2,y2,z2,speed,background=False):
        #run it in its own thread
        fireThread = Thread(None, self._fire, None, (x1, y1, z1, x2, y2, z2, speed))
        fireThread.start()
        
        #if backgroud == True, return the thread, otherwise wait for it to finish
        if background == False:
            fireThread.join()

        return fireThread

    def _fire(self,x1,y1,z1,x2,y2,z2,speed):
        
        startPos = Vec3(x1,y1,z1)
        projectileShape = MinecraftShape(self.mc, startPos, self.projectileBlocks)

        mcDraw = MinecraftDrawing(self.mc)
        blocksBetween = mcDraw.getLine(x1, y1, z1, x2, y2, z2)

        for blockBetween in blocksBetween:
            projectileShape.move(blockBetween.x, blockBetween.y, blockBetween.z)
            # time to sleep between each block move
            sleep(speed)
            
        projectileShape.clear()


class XWingMissile(Projectile):

    def __init__(self):
        missileBlocks = [ShapeBlock(0,0,0,block.TNT)]
        Projectile.__init__(self, missileBlocks)

