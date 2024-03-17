import RPi.GPIO as GPIO
import time

radius_max = 25.5 #en mm
ratio = 0.512
i1 = 64
i2 = 125

class Motor():
    def __init__(self, motor_pins, log=False):
        in1, in2, in3, in4 = motor_pins
        self.step_sleep = 0.002
        self.log = log
        # self.step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°
        self.step_sequence = [[1,0,0,1],
                            [1,0,0,0],
                            [1,1,0,0],
                            [0,1,0,0],
                            [0,1,1,0],
                            [0,0,1,0],
                            [0,0,1,1],
                            [0,0,0,1]]

        GPIO.setmode( GPIO.BCM )
        GPIO.setup( in1, GPIO.OUT )
        GPIO.setup( in2, GPIO.OUT )
        GPIO.setup( in3, GPIO.OUT )
        GPIO.setup( in4, GPIO.OUT )

        GPIO.output( in1, GPIO.LOW )
        GPIO.output( in2, GPIO.LOW )
        GPIO.output( in3, GPIO.LOW )
        GPIO.output( in4, GPIO.LOW )

        self.motor_pins = [in1,in2,in3,in4]
        self.motor_step_counter = 0 

    def off(self):
        GPIO.output( self.motor_pins[1], GPIO.LOW )
        GPIO.output( self.motor_pins[2], GPIO.LOW )
        GPIO.output( self.motor_pins[3], GPIO.LOW )
        GPIO.output( self.motor_pins[0], GPIO.LOW )
        GPIO.cleanup()

    def move(self, steps, direction):
            self.refresh_log(steps)
            for _ in range(steps):
                for pin in range(len(self.motor_pins)):
                    GPIO.output(self.motor_pins[pin], self.step_sequence[self.motor_step_counter][pin])

                if direction:
                    self.motor_step_counter = (self.motor_step_counter - 1) % 8
                else:
                    self.motor_step_counter = (self.motor_step_counter + 1) % 8

                time.sleep(self.step_sleep)

    def move_mm(self,distance):
         total_steps = self.get_total_step()
         radius = radius_max - total_steps/(i1*i2*ratio)
         angle = (distance*i1*i2)/radius
         step = angle*4096/(2*3.142592)
         self.move(step,True)

    def refresh_log(self,steps):
        if self.log:
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
    # Utilisation de la classe Motor
    in1 = 17
    in2 = 18
    in3 = 27
    in4 = 22
    pins_list = [in1, in2, in3, in4]
    motor = Motor(pins_list, True)
    motor.erase_log()