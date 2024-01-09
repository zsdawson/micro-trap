import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep, strftime
import os

# GPIO setup
trigger_pin = 17  # Replace with your GPIO pin number
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.IN)

camera = PiCamera()

def take_picture():
    timestamp = strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'/home/pi/photos/photo_{timestamp}.jpg'
    camera.capture(filename)
    print(f"Photo taken: {filename}")

try:
    while True:
        if GPIO.input(trigger_pin):
            take_picture()
            sleep(1)  # Delay to avoid multiple triggers

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
