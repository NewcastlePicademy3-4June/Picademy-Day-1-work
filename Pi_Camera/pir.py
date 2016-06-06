#uses the camera module to take a photo when the PIR sensor detects movement

from picamera import PiCamera
from time import sleep
from gpiozero import MotionSensor

camera = PiCamera()
sensor=MotionSensor(4)
n=0

camera.start_preview(alpha=200)
sensor.wait_for_motion()
n=n+1
camera.capture("/home/pi/Desktop/pir"+str(n)+".jpg")
camera.stop_preview()
