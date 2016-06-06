#Minecraft Steve trapdoor

#import required modules
from mcpi.minecraft import Minecraft
import time
from time import sleep
import random
import explorerhat
from mcpi import block

#declare and assign variables
mc=Minecraft.create()
global player_choice
earth = [-128,-128,-128,128,0,128,1]
mc.setBlocks (earth)

sky = [-128,0,-128,128,128,128,0]
mc.setBlocks (sky)

mc.player.setPos(-19,0,-16)

trapBase = [-10,0,-10,10,20,10,17]
mc.setBlocks (trapBase)
trapBaseHollow = [-9,-130,-9,9,20,9,00]
mc.setBlocks (trapBaseHollow)
trapDoor = [-9,20,-9,9,20,9,57]
mc.setBlocks (trapDoor)
trapDoorGone = [-9,20,-9,9,20,9,0]
blockType = (53,0)

#handler for explorer hat button 1 press
def touch_1(channel,event):
    global player_choice
    global computer_choice
    computer_choice=random.randint(1,4)
    mc.postToChat("You chose 1...")
    player_choice=1
    if player_choice == computer_choice:
        survive()
    else:
        mc.setBlocks(trapDoorGone)
        dead()
        time.sleep(0.2)
        mc.setBlocks(trapDoor)

#handler for explorer hat button 2 press
def touch_2(channel,event):
    global player_choice
    global computer_choice
    computer_choice=random.randint(1,4)
    mc.postToChat("You chose 2...")
    player_choice=2
    if player_choice == computer_choice:
        survive()
    else:
        mc.setBlocks(trapDoorGone)
        dead()
        time.sleep(0.2)
        mc.setBlocks(trapDoor)
        dead()

#handler for explorer hat button 3 press        
def touch_3(channel,event):
    global player_choice
    global computer_choice
    computer_choice=random.randint(1,4)
    mc.postToChat("You chose 3...")
    player_choice=3
    if player_choice == computer_choice:
        survive()
    else:
        mc.setBlocks(trapDoorGone)
        dead()
        time.sleep(0.2)
        mc.setBlocks(trapDoor)

#handler for explorer hat button 4 press    
def touch_4(channel,event):
    global player_choice
    global computer_choice
    computer_choice=random.randint(1,4)
    mc.postToChat("You chose 4...")
    player_choice=4
    if player_choice == computer_choice:
        survive()
    else:
        mc.setBlocks(trapDoorGone)
        dead()
        time.sleep(0.2)
        mc.setBlocks(trapDoor)

#create stairs on tower
def ewstairs(x,y,z):
    blockType = (53,0)
    for i in range(21):
        mc.setBlock(x,y,z,blockType)
        x=x+1
        y=y+1
ewstairs(-10,0,-11)

def westairs(x,y,z):
    blockType = (53,1)
    for i in range(21):
        mc.setBlock(x,y,z,blockType)
        x=x-1
        y=y+1
westairs(10,0,11)

def snstairs(x,y,z):
    blockType = (53,2)
    for i in range(21):
        mc.setBlock(x,y,z,blockType)
        z=z+1
        y=y+1
snstairs(11,0,-10)

def nsstairs(x,y,z):
    blockType = (53,3)
    for i in range(21):
        mc.setBlock(x,y,z,blockType)
        z=z-1
        y=y+1
nsstairs(-11,0,10)


#detect if Steve is standing on diamond blocks to activate trap
#request user input from explorerhat buttons
def start():
    diamonds=True
    while diamonds==True:
        pos = mc.player.getPos()
        blockType = mc.getBlock(pos.x, pos.y-1, pos.z)
        if blockType == 57:
            diamonds==False
            mc.postToChat("TRAP ACTIVATED!")
            mc.postToChat("To escape, you must choose a number between 1 and 4")
            mc.postToChat("Choose correctly and you are free to leave...")
            mc.postToChat("...but choose incorrectly and...")
            mc.postToChat("Use the explorer hat buttons to make your choice")
            explorerhat.light.blue.on()
            sleep(0.3)
            explorerhat.light.blue.off()
            sleep(0.3)
            explorerhat.light.yellow.on()
            sleep(0.3)
            explorerhat.light.yellow.off()
            sleep(0.3)
            explorerhat.light.red.on()
            sleep(0.3)
            explorerhat.light.red.off()
            sleep(0.3)      
            explorerhat.light.green.on()
            sleep(0.3)
            explorerhat.light.green.off()
            explorerhat.touch.one.pressed(touch_1)
            explorerhat.touch.two.pressed(touch_2)
            explorerhat.touch.three.pressed(touch_3)
            explorerhat.touch.four.pressed(touch_4) 

            
        else:

    
            time.sleep(0.2)
            mc.setBlocks (trapDoor)
        


#if player guesses correctly

def survive():
    mc.postToChat("You survived...!")
    mc.postToChat("...THIS TIME!")
    start()

#if playerguesses incorrectly
def dead():
    mc.postToChat("Dead!")
    explorerhat.motor.one.forward(50)
    sleep(0.3)
    explorerhat.motor.one.stop()
    sleep(0.3)
    explorerhat.motor.one.backward(50)
    sleep(0.3)
    explorerhat.motor.one.stop()
    
#call start function to run program
start()
    
