#turns a motor on and off using the explorer hat
import explorerhat
from time import sleep

explorerhat.motor.one.forward(100)

sleep(5)

explorerhat.motor.one.stop()
