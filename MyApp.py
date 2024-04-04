from Camera import *
from Fan import *
from Led import *
from Button import *
from MotorTransport import *
from datetime import datetime
import os


class MyApp():

    def __init__(self, fan_pin, led_pins, motor_pins, camera_motor_pins, button_pin):
        self.run = True
        self.fan = Fan(fan_pin)
        self.date = datetime.today().strftime("%Y-%m-%d")
        self.led = Led(led_pins)
        self.transportMotor = MotorTransport(motor_pins)
        self.camera = Camera(camera_motor_pins)
        self.button = Button(button_pin)
        self.button.on_single_click(self.button_single_click)
        self.button.on_double_click(self.button_double_click)
        self.init_storage()

    def routine(self):
        self.run = True
        start_time = time.time()
        self.fan.start_on()
        while self.run :
            current_time = time.time()
            t = current_time - start_time
            if t < (6*3600) :       # 6 hrs of pollen trapping
                self.led.on(0,1,1) # yellow
                self.fan.on()
                time.sleep(0.1)
            else :
                self.led(0,0,1) # blue
                self.transportMotor.move_mm(100)
                for i in range(4):
                    self.camera.take_3_pictures("Image/" + self.date,self.date+ f"_{i}")
                self.run = False
        self.led.on_for(0,1,0, 10) # green for 10sec

    def routine_test(self):
        self.run = True
        start_time = time.time()
        self.fan.start_on()
        while self.run :
            current_time = time.time()
            t = current_time - start_time
            if t < 60 :       # 60 sec of pollen trapping
                self.led.on(0,1,1) # yellow
                self.fan.on()
                time.sleep(0.1)
            else :
                self.led(0,0,1) # blue
                self.transportMotor.move(2000, True)
                for i in range(4):
                    self.camera.take_3_pictures("Image/" + self.date,self.date+ f"_{i}")
                self.run = False
        self.led.on_for(0,1,0, 10) # green for 10sec

    def init_storage(self):
        os.mkdir("Image/" + self.date)

    def button_single_click(self):
        self.run = False

    def button_double_click(self):
        self.transportMotor.erase_log()
    
    def off(self):
        self.fan.off()
        self.led.off()
        self.transportMotor.off()
        self.camera.off()
        GPIO.cleanup()

if __name__ == "__main__" :
    date = datetime.today().strftime("%Y-%m-%d")
    os.mkdir("Image/" + date)