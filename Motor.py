import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Set GPIO pin for fan control
PIN = 16
GPIO.setup(PIN, GPIO.OUT)

class Motor():
    