import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Set GPIO pin for fan control
fan_pin = 18
GPIO.setup(fan_pin, GPIO.OUT)

class Fan():
        
    def on(self):
        GPIO.output(fan_pin, GPIO.HIGH)

    def off(self):
        GPIO.output(fan_pin, GPIO.LOW)