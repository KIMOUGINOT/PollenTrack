import RPi.GPIO as GPIO
import time

PWM_FREQ = 3853   
duty_cycle = 5.04
duty_cycle_start = 100 

class Fan():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)                                                     
        self.pwm = GPIO.PWM(pin, PWM_FREQ)
        self.pwm.start(0)
        
    def start_on(self) :
        self.pwm.ChangeDutyCycle(duty_cycle_start) # Start strong to give momentum to the fan
        time.sleep(1)

    def on(self) :   
        self.pwm.ChangeDutyCycle(duty_cycle) # Then set the wanted duty cycle
    
    def on_for(self, duration):
        """ Turn on the fan during the time given in parameters

        Args:
            duration (_float_): in seconds
        """
        self.pwm.ChangeDutyCycle(duty_cycle_start) # Start strong to give momentum to the fan
        time.sleep(1)
        self.pwm.ChangeDutyCycle(duty_cycle) # Then set the wanted duty cycle
        time.sleep(duration)

    def off(self):
        """ Turn off the fan
        """
        self.pwm.stop()