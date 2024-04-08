from MyApp import *

if __name__ == "__main__":

    fan_pin = 9 #inserer les pins
    led_pins = [23, 24, 10] #inserer les pins
    camera_pins = [2, 3, 4, 14]
    motor_pins = [15, 18] #inserer les pins
    button_pin = 11 #inserer les pins
    led_microscope_pin = [8, 0, 0] 

    cycle = MyApp(fan_pin, led_pins, motor_pins, camera_pins, button_pin)
    cycle.routine_test()
    cycle.off()
     