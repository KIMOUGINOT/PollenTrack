import RPi.GPIO as GPIO
import time

class Motor():
    def __init__(self, in1, in2, in3, in4):
        self.step_sleep = 0.002
        self.step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°
        self.direction = False # True for clockwise, False for counter-clockwise
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

        # initializing
        GPIO.output( in1, GPIO.LOW )
        GPIO.output( in2, GPIO.LOW )
        GPIO.output( in3, GPIO.LOW )
        GPIO.output( in4, GPIO.LOW )

        self.motor_pins = [in1,in2,in3,in4]
        self.motor_step_counter = 0 

    def cleanup(self):
        GPIO.output( self.motor_pins[1], GPIO.LOW )
        GPIO.output( self.motor_pins[2], GPIO.LOW )
        GPIO.output( self.motor_pins[3], GPIO.LOW )
        GPIO.output( self.motor_pins[4], GPIO.LOW )
        GPIO.cleanup()

    def move(self, steps, direction):
            if direction:
                self.direction = True
            else:
                self.direction = False

            for _ in range(steps):
                for pin in range(len(self.motor_pins)):
                    GPIO.output(self.motor_pins[pin], self.step_sequence[self.motor_step_counter][pin])

                if self.direction:
                    self.motor_step_counter = (self.motor_step_counter - 1) % 8
                else:
                    self.motor_step_counter = (self.motor_step_counter + 1) % 8

                time.sleep(self.step_sleep)

if __name__ == "__main__":
    # Utilisation de la classe Motor
    in1 = 17
    in2 = 18
    in3 = 27
    in4 = 22
    motor = Motor(in1, in2, in3, in4)
    try:
        # Déplacer de 100 pas dans la direction spécifiée
        motor.move(100, direction=True)  # ou False pour changer la direction
    except KeyboardInterrupt:
        motor.cleanup()