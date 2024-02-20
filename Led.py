import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Set GPIO pins for led control
RED_PIN = 11
GREEN_PIN = 13
BLUE_PIN = 15
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

class Led():
        
    def on(self, red, green, blue):
        GPIO.output(RED_PIN, red)
        GPIO.output(GREEN_PIN, green)
        GPIO.output(BLUE_PIN, blue)

    def off(self):
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(BLUE_PIN, GPIO.LOW)