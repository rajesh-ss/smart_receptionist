import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Servo

servo = Servo(2)
val = -1

try:
    while True:
        servo.value = val
        sleep(0.1)
        val = val + 0.09
        if val > 1:
            val = -1
except KeyboardInterrupt:
	print("Program stopped")