import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as mcstuff
from time import sleep

class Planet():
    def __init__(self, pos, radius, blockType, blockData = 0):
        self.mc = minecraft.Minecraft.create()
        self.pos = pos
        self.radius = radius
        self.blockType = blockType
        self.blockData = blockData
        self._draw()

    def _draw(self):
        mcDraw = mcstuff.MinecraftDrawing(self.mc)
        mcDraw.drawHollowSphere(self.pos.x, self.pos.y, self.pos.z,
                                self.radius, self.blockType, self.blockData)
    
    def destroy(self, delay):
        mcDraw = mcstuff.MinecraftDrawing(self.mc)
        #mcDraw.drawHollowSphere(self.pos.x, self.pos.y, self.pos.z,
        #                        self.radius, block.LAVA_STATIONARY.id)
        #sleep(delayLava)
        mcDraw.drawHollowSphere(self.pos.x, self.pos.y, self.pos.z,
                                self.radius, block.COBBLESTONE.id)
        sleep(delay)
        self.clear()

    def clear(self):
        mcDraw = mcstuff.MinecraftDrawing(self.mc)
        mcDraw.drawSphere(self.pos.x, self.pos.y, self.pos.z,
                                self.radius, block.AIR.id)
