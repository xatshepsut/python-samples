import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.cleanup()

led = 4

GPIO.setup(led, GPIO.OUT)

is_on = False
count = 25

while count:
   	time.sleep(0.5)
	GPIO.output(led, GPIO.LOW if is_on else GPIO.HIGH)
	is_on = False if is_on else True
	count = count - 1

GPIO.cleanup()

