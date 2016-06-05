#A 3 LED traffic light sequence activate dby a button press
from gpiozero import LED, Button
from time import sleep

led_red = LED(17)
led_yellow = LED(27)
led_green = LED(22)
button= Button(5)
while True:
    button.wait_for_press()
    for n in range (3):
        led_red.on()
        led_yellow.off()
        sleep(1)
        led_yellow.on()
        sleep(1)
        led_red.off()
        led_yellow.off()
        led_green.on()
        sleep(1)
        led_green.off()
        led_yellow.on()
        led_red.off()
        sleep(1)
        led_red.on()
        led_yellow.off()
        sleep(1)
        led_red.off()
