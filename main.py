from MyApp import *

if __name__ == "__main__":

    fan_pin = 0 #inserer les pins
    led_pins = [0, 0, 0] #inserer les pins
    camera_pins = [22, 27, 17, 23]
    motor_pins = [0, 0] #inserer les pins
    button_pin = 0 #inserer les pins

    cycle = MyApp(fan_pin, led_pins, motor_pins, camera_pins, button_pin)
    cycle.routine_test()
    cycle.off()
     