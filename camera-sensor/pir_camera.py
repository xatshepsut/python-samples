import RPi.GPIO as GPIO
import time
import subprocess

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

# Usually first image is corrupted, passing corrupted shot
print("Making test shot...")
subprocess.call(['./camera.sh'])
            
while True:
    #print("Sleeping before next detection...")
    time.sleep(0.6)
    #print("Checking sensor state...")
    previous_state = current_state
    current_state = GPIO.input(sensor)

    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        print("GPIO pin %s is %s" % (sensor, new_state))

        if current_state:
            print("Motion detected, making photo...")
            subprocess.call(['./camera.sh'])
            print("Done...")
    #print("Last line inside loop...")

