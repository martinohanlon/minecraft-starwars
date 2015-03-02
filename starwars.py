#Minecraft Star Wars
#Martin O'Hanlon
#www.stuffaboutcode.com

from deathstar import DeathStar
from starwarscraft import TieFighter, MilleniumFalcon, XWingFighter, XWingFighterDiagonal
from planet import Planet
from trench import Trench
from projectile import XWingMissile
from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi import block
from time import sleep

#Main program

#create connection to minecraft
mc = Minecraft.create()

pos = Vec3(0,30,0)
mc.player.setTilePos(pos.x + 25 ,pos.y + 20, pos.z + 25)

#create Alderaan
alderaanPos = pos.clone()
alderaanPos.x += 50
alderaanPos.z += 50
alderaan = Planet(alderaanPos, 10, block.WOOL.id, 3)

#create DeathStar
sleep(15)
deathstarPos = pos.clone()
deathstar = DeathStar(deathstarPos, 15)
sleep(12)
mc.postToChat("Not Alderaan, we are peaceful, we have no weapons.")

#blow up Alderaan
sleep(3)
deathstar.fire(alderaanPos.x, alderaanPos.y, alderaanPos.z, 0.5, 1)
alderaan.destroy(2)

#millenium falcon arrives
sleep(10)
falconPos = pos.clone()
falconPos.z -= 50
falcon = MilleniumFalcon(falconPos)
mc.postToChat("Thats no moon, its a space station")
falcon.fly(pos.x, pos.y, pos.z, 0.5)

#millenium falcon is chased from the death star by tie fighters
sleep(10)
falconFly = falcon.fly(pos.x, pos.y, pos.z + 50, 0.3, True)
mc.postToChat("Sure hope the old man got that tractor beam out of commission, or this is gonna be a real short trip")

#tie fighters take chase
sleep(5)
tie1Pos = pos.clone()
tie1Pos.x -= 5
tie2Pos = pos.clone()
tie2Pos.x += 5
tie1 = TieFighter(tie1Pos)
tie2 = TieFighter(tie2Pos)
tie1Fly = tie1.fly(tie1Pos.x, tie1Pos.y, tie1Pos.z + 50, 0.25, True)
tie2Fly = tie2.fly(tie2Pos.x, tie2Pos.y, tie2Pos.z + 50, 0.25, True)

#wait for falcon and tie fighters to stop
falconFly.join()
falcon.clear()
tie1Fly.join()
tie2Fly.join()
tie1.clear()
tie2.clear()
mc.postToChat("They let us go. It was the only reason for the ease of our escape.")

#create Yavin 4
sleep(10)
yavinPos = pos.clone()
yavinPos.x -= 60
yavinPos.z += 60
yavin = Planet(yavinPos, 10, block.WOOL.id, 13)

#x wing fighter attacks
sleep(5)
xWing1Pos = pos.clone()
xWing1Pos.x -= 50
xWing1Pos.z += 50
xWing1 = XWingFighterDiagonal(xWing1Pos)
xWing1.fly(pos.x - 10, pos.y, pos.z + 10, 0.25)
xWing1.clear()

#fly x wing down the treach
trenchPos = Vec3(50,40,-50)
trench = Trench(trenchPos, 14, 8, 100)

#put the player in the trench
mc.player.setTilePos(57, 41, 49)
sleep(2)

xWing2Pos = Vec3(57, 44, 45)
xWing2 = XWingFighter(xWing2Pos)
xWing2Fly = xWing2.fly(57, 44, -25, 0.25, True)

#fire the missile at the exhaust port
sleep(12)
mc.postToChat("Use the force Luke")
sleep(1)
missile = XWingMissile()
missileFire = missile.fire(xWing2.position.x, xWing2.position.y, xWing2.position.z - 3,
                           trench.exhaustPortPos.x, trench.exhaustPortPos.y, trench.exhaustPortPos.z,
                           0.1, True)

#wait for the missile and the xwing to stop
missileFire.join()
xWing2Fly.join()
xWing2.clear()
trench.clear()

#move player back above deathstar
mc.player.setTilePos(pos.x, pos.y + 20, pos.z)

#xwing escapes from deathstar
xWing3Pos = pos.clone()
xWing3Pos.z -= 10 
xWing3 = XWingFighter(xWing1Pos)
xWing3Fly = xWing3.fly(pos.x, pos.y, pos.z - 50, 0.25, True)
sleep(3)

#destroy the deathstar
deathstar.destroy()
sleep(5)
mc.postToChat("duh der der duh, der, duh der der duh, der, der der der der der")
sleep(10)

#finish by clearing xwing and yavin
xWing3Fly.join()
xWing3.clear()
yavin.clear()

