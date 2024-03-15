import RPi.GPIO as GPIO

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
        """ Turn on the led according to the colors chosen

        Args:
            red (_bool_)
            green (_bool_) 
            blue (_bool_)
        """
        GPIO.output(self.red_pin, red)
        GPIO.output(self.green_pin, green)
        GPIO.output(self.blue_pin, blue)

    def on_for(self, red, green, blue, duration) :
        """ Turn on the led according to the colors chosen during the time given in parameters

        Args:
            red (_bool_)
            green (_bool_) 
            blue (_bool_)
            duration (_float_): Duration in seconds
        """
        self.on(red, green, blue)
        time.sleep(duration)
        self.off()

    def off(self):
        """ Turn off the led
        """
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
