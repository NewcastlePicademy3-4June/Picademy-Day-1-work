#takes a picture with picam when a button is pressed

from picamera import PiCamera
from time import sleep
from gpiozero import Button, LED

camera = PiCamera()
button=Button(17)
led=LED(27)
n=0

while True:
    camera.start_preview(alpha=200)
    button.wait_for_press()
    n=n+1
    for x in range(3):
        led.on()
        sleep(0.3)
        led.off()
        sleep(0.3)
    camera.capture("/home/pi/Desktop/button"+str(n)+".jpg")
    camera.stop_preview()
