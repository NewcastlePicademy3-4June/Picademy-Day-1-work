#takes a picture very 3 seconds
from picamera import PiCamera
from time import sleep

camera = PiCamera()

sleep(3)
camera.capture("/home/pi/Desktop/selfie0.jpg")
sleep(3)
camera.capture("/home/pi/Desktop/selfie1.jpg")
sleep(3)
camera.capture("/home/pi/Desktop/selfoe2.jpg")
