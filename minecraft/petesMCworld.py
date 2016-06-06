#creates a trail of random blocks from the which_brick list behind the player
from mcpi.minecraft import Minecraft
from mcpi import block
import random
mc=Minecraft.create()
while True:
    pos=mc.player.getPos()
    which_brick = random.choice([block.STONE.id,block.DIRT.id, block.MUSHROOM_RED.id])
    mc.setBlock(pos.x-1, pos.y, pos.z, which_brick)
    
