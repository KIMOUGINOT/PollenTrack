import RPi.GPIO as GPIO
import time

# radius_max = 25.5 #en mm
# ratio = 0.512
# i1 = 64
# i2 = 125

class MotorTransport():
    def __init__(self, motor_pins):
        self.dirPin, self.stepPin = motor_pins
        self.speed = 0.0005

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.dirPin, GPIO.OUT)
        GPIO.setup(self.stepPin, GPIO.OUT)

    def off(self):
        GPIO.cleanup()

    def move(self, steps, direction):
        if direction:
            self.refresh_log(steps)
            GPIO.output(self.dirPin, GPIO.HIGH)
        else:
            GPIO.output(self.dirPin, GPIO.LOW)

        for _ in range(steps):
            GPIO.output(self.stepPin, GPIO.HIGH)
            time.sleep(self.speed) 
            GPIO.output(self.stepPin, GPIO.LOW)
            time.sleep(self.speed)

    # def move_mm(self,distance):  /* à refaire totalement */
    #      total_steps = self.get_total_step()
    #      radius = radius_max - total_steps/(i1*i2*ratio)
    #      angle = (distance*i1*i2)/radius
    #      step = angle*4096/(2*3.142592)
    #      self.move(step,True)

    def refresh_log(self,steps):
        total_steps = self.get_total_step()
        with open("motor_utilities/log.txt", "w") as file:
            file.write(str(steps + total_steps))

    def erase_log(self):
        with open("motor_utilities/log.txt", "w") as file:
            file.write(str(0))

    def get_total_step(self):
        with open("motor_utilities/log.txt", "r") as file:
                total_steps = int(file.read())
        return total_steps
                

if __name__ == "__main__":
    # Utilisation de la classe MotorTransport
    in1 = 15
    in2 = 18
    pins_list = [in1, in2]
    motor = MotorTransport(pins_list)
    motor.move(200, True)
    print(motor.get_total_step())
    motor.erase_log()
    motor.off()