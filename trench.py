from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
import mcpi.block as block
import mcpi.minecraftstuff as mcstuff

class Trench:
    def __init__(self, pos, width, height, length):
        self.mc = Minecraft.create()
        
        self.pos = pos
        self.width = width
        self.height = height
        self.length = length

        self._draw()

    def _draw(self):

        pos = self.pos
        mc = self.mc
        width = self.width
        height = self.height
        length = self.length

        #create trench
        mc.setBlocks(pos.x, pos.y, pos.z,
                     pos.x + width, pos.y + height, pos.z + length,
                     block.WOOL.id, 15)

        mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1,
                     pos.x + width - 1, pos.y + height, pos.z + length - 1,
                     block.AIR.id)

        #find the exhaust port position
        self.exhaustPortPos = Vec3(pos.x + (width / 2),
                                   pos.y + (height / 2),
                                   pos.z + 1)
        
        #draw exhaust post
        mcDraw = mcstuff.MinecraftDrawing(self.mc)
        mcDraw.drawCircle(self.exhaustPortPos.x,
                          self.exhaustPortPos.y,
                          self.exhaustPortPos.z,
                          2, block.IRON_BLOCK.id)
        
    def clear(self):

        pos = self.pos
        mc = self.mc
        width = self.width
        height = self.height
        length = self.length
        
        #clear trench
        mc.setBlocks(pos.x, pos.y, pos.z,
                     pos.x + width, pos.y + height, pos.z + length,
                     block.AIR.id)
        
