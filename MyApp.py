from Camera import *
from Fan import *
from Led import *
from datetime import datetime
import os


class MyApp():

    def __init__(self, fan_pin, init_led_pin, transport_led_pin, end_led_pin, motor_pins, camera_motor_pins):
        self.fan = Fan(fan_pin)
        # self.init_led = Led(init_led_pin)
        # self.transport_led = Led(transport_led_pin)
        # self.end_led = Led(end_led_pin)
        self.transportMotor = Motor(motor_pins)
        self.camera = Camera(camera_motor_pins)
        # self.init_storage()

    # def run(self):

    def init_storage():
        date = datetime.today().strftime("%Y-%m-%d")
        os.mkdir("Image/" + date)

if __name__ == "__main__" :
    date = datetime.today().strftime("%Y-%m-%d")
    os.mkdir("Image/" + date)