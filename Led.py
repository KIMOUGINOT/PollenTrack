import RPi.GPIO as GPIO

# Set GPIO pins for led control
RED_PIN = 11
GREEN_PIN = 13
BLUE_PIN = 15

class Led():
    def __init__(self, red_pin, green_pin, blue_pin):
        GPIO.setmode(GPIO.BCM)
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)
        
    def on(self, red, green, blue):
        GPIO.output(self.red_pin, red)
        GPIO.output(self.green_pin, green)
        GPIO.output(self.blue_pin, blue)

    def off(self):
        GPIO.output(self.red_pin, GPIO.LOW)
        GPIO.output(self.green_pin, GPIO.LOW)
        GPIO.output(self.blue_pin, GPIO.LOW)

if __name__ == "__main__" :
    import time
    led = Led(23,24,25)
    led.on(1,0,0)
    time.sleep(1)
    led.on(0,1,0)
    time.sleep(1)
    led.on(0,0,1)
    time.sleep(1)
    led.off()
