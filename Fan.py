import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Set GPIO pin for fan control
PIN = 18
GPIO.setup(PIN, GPIO.OUT)

class Fan():
        
    def on(self):
        GPIO.output(PIN, GPIO.HIGH)

    def off(self):
        GPIO.output(PIN, GPIO.LOW)