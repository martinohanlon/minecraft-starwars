import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

MINX = -100
MAXX = 100
MINZ = -100
MAXZ = 100
MINY = -60
MAXY = 64

mc = minecraft.Minecraft.create()

mc.player.setPos(0,0,0)

for y in range(MAXY, MINY, -1):
    mc.setBlocks(MINX, y, MINZ, MAXX, y, MAXZ, block.AIR.id)
    sleep(1)
    print y

mc.setBlocks(MINX, MINY, MINZ, MAXX, MINY, MAXZ, block.GRASS.id)
