#plants a sapling block whenever the player is walking on a grass block

from mcpi.minecraft import Minecraft
from mcpi import block

mc=Minecraft.create()
while True:
    pos=mc.player.getPos()
    blockType = mc.getBlock(pos.x,pos.y-1,pos.z)
    if blockType == block.GRASS.id:
        max_length = 3
        for length in range(max_length):
            mc.setBlock(pos.x-1+length, pos.y+1, pos.z-1, block.SAPLING.id)
    
    
