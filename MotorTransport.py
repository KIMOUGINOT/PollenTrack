import RPi.GPIO as GPIO
import time

radius_max = 25.5 #en mm
i_m = 1.8/16
full_rotation_step = 3200 # 16 microstep x 200 
scotch_thickness = 28e-6

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

    def move_mm(self,distance):  
         total_steps = self.get_total_step()
         radius = radius_max - (total_steps/3200*scotch_thickness)
         angle = (distance*i_m)/radius
         step = int(angle*full_rotation_step/(2*3.142592))
         self.move(step,False)

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
    motor.move(200, False)
    print(motor.get_total_step())
    motor.move_mm(100)
    motor.erase_log()
    motor.off()