#uses the explorerhat to control a motor when a button is pressed on the explorer hat

import explorerhat
from time import sleep
from random import randint


def wheel(channel, evemt):
    duration = randint(5,15)
    print(duration)
    explorerhat.motor.one.forward(100)
    sleep(duration)
    explorerhat.motor.one.stop()

while True:
    explorerhat.touch.one.pressed(wheel)
