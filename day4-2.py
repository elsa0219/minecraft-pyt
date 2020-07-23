# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:44:11 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
x,y,z=mc.player.getTilePos()
for i in range(20):
    r=random.randrange(1,7)
    
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,241)
        x=x+4
    elif r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,225)
        x=x-4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+4,251,6)
        z+z+4
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z-4,35,6)
        z=z-4
    elif r == 5:
        mc.setBlocks(x,y,z,x,y+4,z,95,6)
        y=y+4
    elif r == 6:
        mc.setBlocks(x,y,z,x,y-4,z,252,6)
        y=y-4